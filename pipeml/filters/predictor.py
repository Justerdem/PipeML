from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Predictor(BaseFilter):
    """Generate predictions for the test set."""

    def __init__(self) -> None:
        super().__init__(name="Predictor")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
