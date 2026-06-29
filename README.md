# Bearing Prognostics Dashboard

[![Tests](https://github.com/prapallegro/bearing-prognostics-dashboard/actions/workflows/tests.yml/badge.svg)](https://github.com/prapallegro/bearing-prognostics-dashboard/actions)


Interactive dashboard for bearing health monitoring and degradation analysis. Built with [Plotly Dash](https://dash.plotly.com/).

## Overview

This dashboard computes a **health indicator** from multivariate vibration features using Principal Component Analysis (PCA) and visualises the degradation trajectory over time against a user-configurable failure threshold.

> **Status:** v0.1.0-alpha — MVP release. RUL prediction and advanced analytics are on the [roadmap](https://github.com/prapallegro/bearing-prognostics-dashboard/issues).

## Quick Start

```bash
# Clone the repository
git clone https://github.com/prapallegro/bearing-prognostics-dashboard.git
cd bearing-prognostics-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py

Open http://localhost:8050 in your browser.

## Features (v0.1.0)

    Health Indicator — PCA-based scalar degradation score from vibration features
    Threshold Monitoring — Interactive failure-threshold slider with visual annotation
    Interactive Plots — Plotly figures with hover tooltips
    Synthetic Demo Data — Built-in generator for out-of-the-box testing

## Architecture
plain

bearing-prognostics-dashboard/
├── app.py              # Application entry point
├── backend/            # Data-processing pipelines
│   └── simple_pca.py   # PCA health indicator
├── components/         # UI layout components
│   ├── layout.py
│   └── sidebar.py
├── plots/              # Plotly figure factories
│   └── health_plot.py
├── tests/              # pytest suite
│   └── test_simple_pca.py
├── .github/
│   └── workflows/
│       └── tests.yml   # GitHub Actions CI
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
└── requirements.txt

## Requirements

    Python 3.9+
    See requirements.txt for package dependencies

## Testing
bash

pytest tests/ -v

## Citation
If you use this software in your research, please cite:
bibtex

@software{bearing_prognostics_2026,
  author = {Allegro, Paula R. P.},
  title = {Bearing Prognostics Dashboard},
  year = {2026},
  url = {https://github.com/prapallegro/bearing-prognostics-dashboard}
}

## License
MIT License — see LICENSE.

## Contributing
Contributions are welcome. Please see CONTRIBUTING.md for guidelines.