from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class ErrorAnalyzer(BaseFilter):
    """Inspect misclassifications and weaknesses."""

    def __init__(self) -> None:
        super().__init__(name="ErrorAnalyzer")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
