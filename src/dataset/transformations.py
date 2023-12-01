import numpy as np


def ToVec(face):
    return np.array(list(map(lambda img: img.reshape(-1, 1), face)))


