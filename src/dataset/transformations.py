def ToVec(face):
    return list(map(lambda img: img.reshape(-1, 1), face))

