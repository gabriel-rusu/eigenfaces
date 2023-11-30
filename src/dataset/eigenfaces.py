import os
from PIL import Image
import numpy as np


class EigenFaces:

    def __init__(self, data_path, split):
        self.data_path = data_path
        self.split = split
        self.current_idx = 0
        self.images = self.__load_images()

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

    def __transform_to_vec(self):
        for person_face in self.images:
            self.images[person_face] = list(map(lambda img: img.reshape(-1, 1), self.images[person_face]))
        return self.images

    def __compute_average(self):
        average_face = {}
        for person_face in self.images:
            person_faces = self.images[person_face]
            average_face[person_face] = np.sum(person_faces, axis=0) / len(person_faces)
        return average_face

    def normalize_dataset(self):
        mean = self.__compute_average()
        for person_face in self.images:
            if type(mean) == dict:
                self.images[person_face] = list(map(lambda face: face - mean[person_face], self.images[person_face]))
            else:
                self.images[person_face] = list(map(lambda face: face - mean, self.images[person_face]))
        return self.images

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= len(self.images):
            self.current_idx = 0
            raise StopIteration
        else:
            idx = self.current_idx
            self.current_idx += 1
            return self.images[idx]
