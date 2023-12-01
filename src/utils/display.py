import cv2
import numpy as np


def face_from_projection(projection):
    img = projection.real
    return img.reshape(40, 30)


def save_face(face, file_name='face', extenstion='png'):
    cv2.imwrite(f'{file_name}.{extenstion}', np.uint8(face))