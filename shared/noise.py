import numpy as np


def add_gaussian_noise(x, std: float, rng_seed: int = 42):
    rng = np.random.default_rng(rng_seed)
    return x + rng.normal(0.0, std, size=len(x))
