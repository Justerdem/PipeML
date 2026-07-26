from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class TrainTestSplitter(BaseFilter):
    """Split the data into train and test sets."""

    def __init__(self, test_size: float = 0.2, random_state: int = 42) -> None:
        super().__init__(name="TrainTestSplitter")
        self.test_size = test_size
        self.random_state = random_state

    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
