from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataLoader(BaseFilter):
    """Load a built-in scikit-learn dataset."""

    def __init__(self, dataset_name: str = "breast_cancer") -> None:
        super().__init__(name="DataLoader")
        self.dataset_name = dataset_name

    def run(self, context: PipelineContext | None = None) -> PipelineContext:
        raise NotImplementedError
