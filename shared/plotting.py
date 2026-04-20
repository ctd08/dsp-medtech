from pathlib import Path
import matplotlib.pyplot as plt


def save_time_plot(t, x, title: str, output_path: str) -> None:
    """Save a simple time-domain plot."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 4))
    plt.plot(t, x)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
