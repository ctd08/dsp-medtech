import numpy as np


def time_vector(duration_s: float, fs_hz: float) -> np.ndarray:
    n_samples = int(duration_s * fs_hz)
    return np.arange(n_samples) / fs_hz


def sine_wave(freq_hz: float, amplitude: float, phase_rad: float, duration_s: float, fs_hz: float):
    t = time_vector(duration_s, fs_hz)
    x = amplitude * np.sin(2 * np.pi * freq_hz * t + phase_rad)
    return t, x
