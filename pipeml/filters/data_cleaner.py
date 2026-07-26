from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataCleaner(BaseFilter):
    """Clean the feature matrix."""

    def __init__(self) -> None:
        super().__init__(name="DataCleaner")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
