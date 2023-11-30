import os
from pathlib import Path
from typing import Final


class Paths:
    BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = os.path.join(BASE_DIR, 'data')


class DatasetSplit:
    TRAIN = 'train'
    TEST = 'test'

class DatasetStatistics:
    MEAN: Final[str] = 'mean'
    STD: Final[str] = 'std'