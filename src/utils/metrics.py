import numpy as np
from tqdm.notebook import tqdm

from src.utils.covariance import compute_eigen_space_distance


def compute_accuracy(test_dataset, train_eigen_matrices, mean_train_faces, logging=False, notebook=False):
    wrong = 0
    correct = 0
    iterable = tqdm(test_dataset) if notebook else test_dataset

    for face_idx, person_faces in enumerate(iterable, 1):

        for face in person_faces:
            min_diff = None
            prediction = None
            for idx in train_eigen_matrices:
                projected_face = compute_eigen_space_distance(face, train_eigen_matrices[idx], mean_train_faces[idx])
                dist = np.linalg.norm(projected_face)
                if min_diff is None:
                    min_diff = dist
                    prediction = idx
                elif min_diff > dist:
                    min_diff = dist
                    prediction = idx
            if prediction == face_idx:
                correct += 1
            else:
                wrong += 1

            if logging:
                print('Predicted: {} - Real: {}'.format(prediction, face_idx))

    print('Correct: {} - Wrong: {} - Accuracy: {:.2f}%'.format(correct, wrong, correct * 100 / (correct + wrong)))