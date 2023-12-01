import os
from PIL import Image
import numpy as np

from src.dataset.transformations import ToVec
from src.utils.constants import Paths, DatasetSplit


class EigenFaces:

    def __init__(self, data_path, split, normalize=False):
        self.data_path = data_path
        self.split = split
        self.current_idx = 1
        self.transformations = [ToVec]
        self.images = self.__load_images()
        self.mean_faces = self.__compute_average()
        if normalize:
            self.__normalize_dataset()

    def __load_images(self):
        path = os.path.join(self.data_path, self.split)
        images = {}
        for file in filter(lambda file: not file.startswith('.'), os.listdir(path)):
            img = Image.open(os.path.join(path, file))
            idx = int(file.split('_')[0])
            if not idx in images:
                images[idx] = []
            images[idx].append(np.asarray(img))

        return images

    def __apply_transform(self, image):
        if self.transformations:
            for transformation in self.transformations:
                image = transformation(image)
        return image

    def __compute_average(self):
        average_face = {}
        for person_face in self.images:
            person_faces = ToVec(self.images[person_face])
            average_face[person_face] = np.sum(person_faces, axis=0) / len(person_faces)
        return average_face

    def __normalize_dataset(self):
        mean = self.__compute_average()
        for person_face in self.images:
            if type(mean) == dict:
                self.images[person_face] = list(
                    map(lambda face: face - mean[person_face], ToVec(self.images[person_face])))
            else:
                self.images[person_face] = list(map(lambda face: face - mean, ToVec(self.images[person_face])))
        return self.images

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx > len(self.images):  # because we start from index 1 of the first person
            self.current_idx = 1
            raise StopIteration
        else:
            idx = self.current_idx
            self.current_idx += 1
            return self.__apply_transform(self.images[idx])

    def __len__(self):
        return len(self.images)