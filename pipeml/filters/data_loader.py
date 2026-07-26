from __future__ import annotations

from sklearn.datasets import load_breast_cancer, load_iris

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataLoader(BaseFilter):
    """Load a built-in sklearn dataset into the pipeline context."""

    def __init__(self, dataset_name: str = "breast_cancer") -> None:
        super().__init__(name="DataLoader")
        self.dataset_name = dataset_name

    def run(self, context: PipelineContext | None = None) -> PipelineContext:
        if context is None:
            context = PipelineContext(dataset_name=self.dataset_name)

        if self.dataset_name == "iris":
            dataset = load_iris(as_frame=False)
        else:
            dataset = load_breast_cancer(as_frame=False)

        context.X = dataset.data.astype(float)
        context.y = dataset.target.astype(int)
        context.feature_names = list(dataset.feature_names)
        context.target_name = "target"
        context.metadata["source"] = self.dataset_name
        self.logger.info("Loaded dataset '%s' with %s samples", self.dataset_name, context.X.shape[0])
        return context
