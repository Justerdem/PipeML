from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Scaler(BaseFilter):
    """Standardize numerical features."""

    def __init__(self) -> None:
        super().__init__(name="Scaler")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
