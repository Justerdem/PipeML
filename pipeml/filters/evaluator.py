from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Evaluator(BaseFilter):
    """Compute evaluation metrics."""

    def __init__(self) -> None:
        super().__init__(name="Evaluator")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
