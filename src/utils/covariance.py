import numpy as np

from src.utils.constants import BestParams


def face_covariance_matrix(face):
    return face * face.T


def compute_face_eigen_matrix(face, num_eigs=14):
    cov_matrix = face_covariance_matrix(face)
    values, vect = np.linalg.eig(cov_matrix)
    indices = []
    while len(indices) < num_eigs:
        index = np.argmax(values)
        np.delete(values, index)
        indices.append(index)
    return vect[:, indices]


def compute_covariance_matrices(dataset):
    cov_matrices = {}
    for idx, person_faces in enumerate(dataset, 1):
        matrices = list(map(lambda face: face_covariance_matrix(face), person_faces))
        for matrix in matrices:
            if idx not in cov_matrices:
                cov_matrices[idx] = matrix
            else:
                cov_matrices[idx] += matrix
        cov_matrices[idx] *= 1 / len(person_faces)
    return cov_matrices


def compute_eigen_matrices(covariance_matrices, num_eigs=BestParams.NUM_EIGEN_VECTORS):
    eigen_matrices = {}
    for matrix in covariance_matrices:
        values, vect = np.linalg.eig(covariance_matrices[matrix])
        indices = [i for i, v in enumerate(values > 0.5) if v]
        indices = indices[:num_eigs]
        eigen_matrices[matrix] = vect[:, indices]
    return eigen_matrices


def compute_eigen_space_distance(image, eigen_matrix, mean):
    identity = np.identity(eigen_matrix.shape[0])

    return (identity - eigen_matrix @ eigen_matrix.T) @ (image - mean)
