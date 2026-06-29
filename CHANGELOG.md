# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Exponential RUL prediction engine with confidence intervals
- Support for WT-HSS, XJTU-SY, and PHM 2012 datasets
- Dark mode and accessibility font scaling
- Spectral kurtosis 3D visualisation
- Feature importance and correlation analysis
- Sphinx documentation and ReadTheDocs hosting


## [0.1.0-alpha] - 2026-06-29

### Added
- Initial MVP release with functional health indicator dashboard
- PCA-based health indicator using scikit-learn
- Interactive Plotly health curve with adjustable failure threshold
- Synthetic vibration feature generator for demonstration
- pytest suite with 4 test cases
- GitHub Actions CI workflow (`.github/workflows/tests.yml`)
- MIT License
- README.md with installation, usage, and citation instructions
- Issue templates (bug report, feature request)
- CHANGELOG.md, CONTRIBUTING.md, and CODE_OF_CONDUCT.md
- Requirements file   

### Known Limitations
- Only synthetic demo data; no real dataset loaders yet
- Single "Health Monitoring" tab; RUL and other views not yet implemented
- Light theme only; dark mode planned for v0.5.0
- No feature engineering pipeline (planned for v0.3.0)
- No spectral analysis (planned for v0.4.0)

[Unreleased]: https://github.com/prapallegro/bearing-prognostics-dashboard/compare/v0.1.0-alpha...HEAD
[0.1.0-alpha]: https://github.com/prapallegro/bearing-prognostics-dashboard/releases/tag/v0.1.0-alpha
