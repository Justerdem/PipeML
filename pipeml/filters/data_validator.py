from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataValidator(BaseFilter):
    """Validate the pipeline context before processing."""

    def __init__(self) -> None:
        super().__init__(name="DataValidator")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
