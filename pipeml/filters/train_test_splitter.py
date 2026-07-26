from __future__ import annotations

from sklearn.model_selection import train_test_split

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class TrainTestSplitter(BaseFilter):
    """Split the dataset into training and test partitions."""

    def __init__(self, test_size: float = 0.2, random_state: int = 42) -> None:
        super().__init__(name="TrainTestSplitter")
        self.test_size = test_size
        self.random_state = random_state

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X is None or context.y is None:
            raise ValueError("The context must contain X and y before splitting")

        X_train, X_test, y_train, y_test = train_test_split(
            context.X,
            context.y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=context.y,
        )
        context.X_train = X_train
        context.X_test = X_test
        context.y_train = y_train
        context.y_test = y_test
        context.metadata["split_config"] = {
            "test_size": self.test_size,
            "random_state": self.random_state,
        }
        self.logger.info("Split data into %s train and %s test samples", len(y_train), len(y_test))
        return context
