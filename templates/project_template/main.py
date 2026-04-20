from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def generate_signal():
    raise NotImplementedError


def add_noise(signal):
    return signal


def process_signal(signal):
    return signal


def analyze_signal(signal):
    return None


def plot_results(*args, **kwargs):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    signal = generate_signal()
    noisy_signal = add_noise(signal)
    processed_signal = process_signal(noisy_signal)
    analyze_signal(processed_signal)
    plot_results(signal, noisy_signal, processed_signal)


if __name__ == "__main__":
    main()
