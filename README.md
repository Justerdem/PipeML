# PipeML

PipeML is a professional-grade, modular machine learning project built with a real Pipe & Filter architecture. It demonstrates how a production-inspired Python pipeline can train and evaluate a classifier while keeping every process stage independent, testable, and reusable.

## Project Overview

This repository is designed to show:

- Python engineering skills with type hints, dataclasses, and clean module boundaries
- Machine learning pipeline fundamentals from loading to reporting
- Pipe & Filter architecture with single-responsibility stages
- Reusable, testable design instead of notebook-based experimentation
- Clear artifact generation for evaluation and model diagnostics

## Features

- Built-in scikit-learn dataset support (Breast Cancer, Iris)
- Structured pipeline with independent filters
- Data validation, cleaning, feature engineering, scaling
- Model training, prediction, evaluation, and error analysis
- Automatic report generation with plots and CSV artifacts
- Configurable pipeline settings via `config.yaml`

## Architecture

The pipeline is organized into independent filters that each accept and return a shared `PipelineContext` dataclass. This prevents hidden state and makes it easy to add, remove, or replace stages.

Key stages:

1. `DataLoader`
2. `DataValidator`
3. `DataCleaner`
4. `FeatureEngineer`
5. `TrainTestSplitter`
6. `Scaler`
7. `ModelTrainer`
8. `Predictor`
9. `Evaluator`
10. `ErrorAnalyzer`
11. `ReportGenerator`

## Pipeline

The orchestrator executes the pipeline in a linear workflow: load data, validate it, clean it, engineer features, split train/test, scale numeric values, train a model, predict on the test set, evaluate results, analyze errors, and persist reports.

## Project Structure

```text
PipeML/
├── config.yaml
├── requirements.txt
├── README.md
├── Architecture.md
├── DesignDecisions.md
├── SequenceDiagram.md
├── UML.md
├── pipeml/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── filters/
│   │   ├── base.py
│   │   ├── data_loader.py
│   │   ├── data_validator.py
│   │   ├── data_cleaner.py
│   │   ├── feature_engineer.py
│   │   ├── train_test_splitter.py
│   │   ├── scaler.py
│   │   ├── model_trainer.py
│   │   ├── predictor.py
│   │   ├── evaluator.py
│   │   ├── error_analyzer.py
│   │   └── report_generator.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── orchestrator.py
│   └── utils/
│       ├── __init__.py
│       └── plotting.py
└── tests/
    ├── test_filters.py
    └── test_orchestrator.py
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the full pipeline:

```bash
python -m pipeml.main
```

## Pipeline output

Running the pipeline produces the following artifacts in the `outputs/` folder:

- `classification_report.txt`
- `metrics.json`
- `confusion_matrix.png`
- `roc_curve.png`
- `feature_importance.png`
- `error_analysis.csv`

## Test suite

Run the unit tests with:

```bash
python -m pytest -q
```

## Sample metrics

The current implementation generates strong baseline performance with metrics such as:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Cross-validation score

## Future work

- Add additional datasets and classifier options
- Add GitHub Actions for CI testing
- Introduce experiment tracking and model versioning
- Add more robust feature engineering and explainability

## Notes for reviewers

This project is intentionally structured to look like a professional codebase instead of a single notebook. The design emphasizes maintainability, modularity, and clear engineering practices.
