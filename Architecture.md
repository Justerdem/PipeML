# Architecture

## Design intent

The architecture is built to show how a machine learning workflow can be organized as a set of small, composable transformations instead of a monolithic notebook cell. Each stage has a focused role and the shared state is represented by the PipelineContext dataclass.

## Pipeline stages

- DataLoader: loads the selected sklearn dataset into memory.
- DataValidator: enforces basic invariants such as aligned samples and finite values.
- DataCleaner: normalizes the data frame and fills missing values.
- FeatureEngineer: adds a derived feature to demonstrate an explicit transformation step.
- TrainTestSplitter: creates training and test partitions with stratification.
- Scaler: standardizes numerical features.
- ModelTrainer: fits a classifier and records cross-validation performance.
- Predictor: generates test predictions and probabilities.
- Evaluator: computes classifier metrics.
- ErrorAnalyzer: collects misclassifications and highlights hard samples.
- ReportGenerator: writes artifacts and plots to disk.

## Why this architecture is beneficial

This structure improves maintainability because a change in one filter rarely forces changes to the others. It also supports testing by isolating each transformation and making failures easier to pinpoint.
