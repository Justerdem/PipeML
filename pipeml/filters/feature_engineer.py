from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class FeatureEngineer(BaseFilter):
    """Add engineered features to the dataset."""

    def __init__(self) -> None:
        super().__init__(name="FeatureEngineer")

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
