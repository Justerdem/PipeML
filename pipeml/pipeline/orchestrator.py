from __future__ import annotations

from pathlib import Path

from pipeml.config import configure_logging, load_config
from pipeml.core.models import PipelineContext
from pipeml.filters.data_cleaner import DataCleaner
from pipeml.filters.data_loader import DataLoader
from pipeml.filters.data_validator import DataValidator
from pipeml.filters.error_analyzer import ErrorAnalyzer
from pipeml.filters.evaluator import Evaluator
from pipeml.filters.feature_engineer import FeatureEngineer
from pipeml.filters.model_trainer import ModelTrainer
from pipeml.filters.predictor import Predictor
from pipeml.filters.report_generator import ReportGenerator
from pipeml.filters.scaler import Scaler
from pipeml.filters.train_test_splitter import TrainTestSplitter


class PipelineOrchestrator:
    """Coordinate the full pipe-and-filter workflow."""

    def __init__(self, output_dir: str | Path | None = None, dataset_name: str = "breast_cancer") -> None:
        self.config = load_config()
        self.output_dir = Path(output_dir or self.config.get("output_dir", "outputs"))
        self.dataset_name = dataset_name
        configure_logging(self.config.get("logging", {}).get("level", "INFO"))

    def run(self) -> dict[str, object]:
        context = PipelineContext(dataset_name=self.dataset_name)

        context = DataLoader(dataset_name=self.dataset_name).run(context)
        context = DataValidator().run(context)
        context = DataCleaner().run(context)
        context = FeatureEngineer().run(context)
        context = TrainTestSplitter(
            test_size=self.config.get("split", {}).get("test_size", 0.2),
            random_state=self.config.get("split", {}).get("random_state", 42),
        ).run(context)
        context = Scaler().run(context)
        context = ModelTrainer(model_name=self.config.get("model", {}).get("name", "random_forest")).run(context)
        context = Predictor().run(context)
        context = Evaluator().run(context)
        context = ErrorAnalyzer().run(context)
        context = ReportGenerator(output_dir=self.output_dir).run(context)

        return {
            "context": context,
            "metrics": context.metrics,
            "report_paths": context.metadata.get("report_paths", {}),
        }
