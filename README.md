# mountain-hmmaxent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Public **code-only** archive for the Remote Sensing of Environment submission.

**GitHub release:** https://github.com/Umutrs16/mountain-hmmaxent-rse/releases/tag/v1.0-rse

Analysis-only code repository for cross-range mountain plant distribution modelling with environmental predictors and Earth-observation embeddings.

This repository intentionally contains **analysis and data-processing code only**. It does not contain manuscript drafting, rewriting, reference-management, Word-generation, cover-letter, or journal-formatting code.

## Included modules

- `validation.py` — leave-one-mountain-range-out and geographic block splits
- `rarefaction.py` — fixed-count training-presence rarefaction
- `residualization.py` — fold-safe removal of environmental signal from embeddings
- `stats.py` — species-cluster bootstrap inference
- `metrics.py` — continuous Boyce index utility
- `conservation.py` — hotspot overlap, Jaccard similarity and protected-area null analysis
- `R/fit_maxnet.R` — MaxEnt/maxnet model fitting wrapper
- `config/analysis.example.yml` — analysis configuration example
- `environment.yml` / `pyproject.toml` — software environment and package metadata

## Installation

```bash
conda env create -f environment.yml
conda activate mountain-hmmaxent
pip install -e .
```

## Examples

```bash
python -m mountain_hmmaxent.cli bootstrap results.csv --value delta_cbi --species species
python -m mountain_hmmaxent.cli jaccard map_cells.csv --a hotspot_m0 --b hotspot_m5
```

Raw third-party datasets are not redistributed. Users should obtain source occurrence, climate, mountain-boundary, satellite-embedding and protected-area datasets from their original providers under the applicable licences.

## License

This software is released under the MIT License.
