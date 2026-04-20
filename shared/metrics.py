import numpy as np


def rms(x) -> float:
    return float(np.sqrt(np.mean(np.asarray(x) ** 2)))
