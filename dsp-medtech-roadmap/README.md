# DSP MedTech Roadmap

A hybrid learning + portfolio repository for rebuilding digital signal processing intuition in Python, with a gradual path toward medtech signal analysis.

## Goals
- practice DSP fundamentals from scratch
- build reusable signal-processing habits
- keep projects small, clear, and repeatable
- grow toward ECG and other medtech-style signals

## Repo structure
- `docs/` learning roadmap and notes
- `shared/` reusable helpers that earn their place after repeated use
- `projects/` numbered mini-projects
- `templates/` starter template for each new project

## Recommended environment
This repo is designed for WSL/Linux-first development.

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python projects/01_sine_wave_basics/main.py
```

## Roadmap projects
1. sine wave basics
2. FFT of mixed signals
3. aliasing experiment
4. noise statistics
5. SNR estimation
6. autocorrelation
7. manual convolution
8. FIR vs IIR
9. moving average filter
10. filter frequency response
11. Butterworth filter
12. ECG simulation
13. ECG filter comparison
14. R-peak detection
15. heart-rate estimation
16. robust peak detection

## Workflow for each project
1. predict what will happen
2. implement the signal pipeline
3. plot time and frequency views
4. write down what changed and why
5. rebuild it later from memory
