from __future__ import annotations

from sklearn.preprocessing import StandardScaler

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Scaler(BaseFilter):
    """Standardize features for model training."""

    def __init__(self) -> None:
        super().__init__(name="Scaler")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X_train is None or context.X_test is None:
            raise ValueError("The context must contain train and test splits")

        scaler = StandardScaler()
        context.X_train = scaler.fit_transform(context.X_train)
        context.X_test = scaler.transform(context.X_test)
        context.metadata["scaler"] = scaler
        self.logger.info("Scaled training and test feature matrices")
        return context
