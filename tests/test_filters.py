import numpy as np

from pipeml.core.models import PipelineContext
from pipeml.filters.data_cleaner import DataCleaner
from pipeml.filters.data_loader import DataLoader
from pipeml.filters.data_validator import DataValidator
from pipeml.filters.feature_engineer import FeatureEngineer
from pipeml.filters.model_trainer import ModelTrainer
from pipeml.filters.predictor import Predictor
from pipeml.filters.scaler import Scaler
from pipeml.filters.train_test_splitter import TrainTestSplitter


def test_data_loader_loads_breast_cancer_dataset():
    loader = DataLoader(dataset_name="breast_cancer")
    context = loader.run()

    assert isinstance(context, PipelineContext)
    assert context.X.shape[0] > 0
    assert context.y.shape[0] > 0
    assert context.X.shape[1] > 1
    assert context.feature_names is not None


def test_pipeline_filters_transform_data():
    loader = DataLoader(dataset_name="breast_cancer")
    context = loader.run()

    validator = DataValidator()
    context = validator.run(context)

    cleaner = DataCleaner()
    context = cleaner.run(context)

    engineer = FeatureEngineer()
    context = engineer.run(context)

    splitter = TrainTestSplitter(test_size=0.2, random_state=42)
    context = splitter.run(context)

    scaler = Scaler()
    context = scaler.run(context)

    trainer = ModelTrainer(model_name="random_forest")
    context = trainer.run(context)

    predictor = Predictor()
    context = predictor.run(context)

    assert context.X_train is not None
    assert context.X_test is not None
    assert context.y_train is not None
    assert context.y_test is not None
    assert context.predictions is not None
    assert len(context.predictions) == len(context.y_test)


def test_scaler_returns_finite_values():
    X = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    scaler = Scaler()
    scaled = scaler._fit_transform(X)

    assert np.isfinite(scaled).all()
    assert scaled.shape == X.shape
