from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class ModelTrainer(BaseFilter):
    """Train the chosen classifier."""

    def __init__(self, model_name: str = "random_forest") -> None:
        super().__init__(name="ModelTrainer")
        self.model_name = model_name

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
