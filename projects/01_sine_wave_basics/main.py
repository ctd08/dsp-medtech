from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from shared.signal_gen import sine_wave


OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def generate_signals():
    fs_hz = 200.0
    duration_s = 1.0

    t, x_5hz = sine_wave(freq_hz=5.0, amplitude=1.0, phase_rad=0.0, duration_s=duration_s, fs_hz=fs_hz)
    _, x_10hz = sine_wave(freq_hz=10.0, amplitude=1.0, phase_rad=0.0, duration_s=duration_s, fs_hz=fs_hz)
    _, x_phase = sine_wave(freq_hz=5.0, amplitude=1.0, phase_rad=np.pi / 4, duration_s=duration_s, fs_hz=fs_hz)

    return t, x_5hz, x_10hz, x_phase, fs_hz


def plot_results(t, x_5hz, x_10hz, x_phase):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(t, x_5hz, label="5 Hz")
    plt.plot(t, x_10hz, label="10 Hz", alpha=0.8)
    plt.plot(t, x_phase, label="5 Hz, phase pi/4", alpha=0.8)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Project 01 - Sine Wave Basics")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sine_wave_basics.png", dpi=150)
    plt.close()


def main():
    t, x_5hz, x_10hz, x_phase, fs_hz = generate_signals()
    plot_results(t, x_5hz, x_10hz, x_phase)
    print(f"Saved plot to: {OUTPUT_DIR / 'sine_wave_basics.png'}")
    print(f"Sampling rate used: {fs_hz} Hz")


if __name__ == "__main__":
    main()
