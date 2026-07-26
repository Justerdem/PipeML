# PipeML

PipeML is a modular machine learning pipeline built around a real Pipe & Filter architecture. The project trains a classifier on the Breast Cancer dataset from scikit-learn and passes every stage of the workflow through independent modules that communicate only through data classes.

## Why this project exists

This repository is designed to demonstrate:

- Python proficiency and clean software design
- Applied machine learning fundamentals and evaluation
- Real Pipe & Filter architecture rather than notebook-centric experimentation
- SOLID-oriented modularity and reusable components

## Architecture at a glance

The workflow is intentionally separated into single-responsibility stages:

1. DataLoader
2. DataValidator
3. DataCleaner
4. FeatureEngineer
5. TrainTestSplitter
6. Scaler
7. ModelTrainer
8. Predictor
9. Evaluator
10. ErrorAnalyzer
11. ReportGenerator

Each stage communicates through the shared PipelineContext dataclass, which prevents hidden shared state and makes the system easy to test and extend.

## Folder structure

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
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Usage

Run the full pipeline:

```bash
python -m pipeml.main
```

The script creates the following output files in the outputs directory:

- classification_report.txt
- metrics.json
- confusion_matrix.png
- roc_curve.png
- feature_importance.png
- error_analysis.csv

## Sample outputs

Expected artifacts are written to the outputs directory after running the pipeline.

## Future improvements

- Add support for additional datasets and algorithms
- Introduce experiment tracking with MLflow
- Add CI/CD with GitHub Actions
- Add model explainability dashboards

## Screenshots placeholder

- Architecture diagram: coming soon
- Evaluation dashboard: coming soon

## Pipe & Filter explanation

A Pipe & Filter architecture is useful here because each stage transforms the data in a predictable, testable way. The design makes the pipeline modular, encourages single-responsibility components, and allows new filters to be inserted without rewriting the rest of the workflow.
