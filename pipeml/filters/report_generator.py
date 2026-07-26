from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class ReportGenerator(BaseFilter):
    """Write evaluation artifacts to disk."""

    def __init__(self, output_dir: str | None = None) -> None:
        super().__init__(name="ReportGenerator")
        self.output_dir = output_dir

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
