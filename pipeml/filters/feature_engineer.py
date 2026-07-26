from __future__ import annotations

import numpy as np

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class FeatureEngineer(BaseFilter):
    """Create a simple interaction feature to demonstrate feature engineering."""

    def __init__(self) -> None:
        super().__init__(name="FeatureEngineer")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X is None:
            raise ValueError("The dataset is missing feature values")

        interaction = np.multiply(context.X[:, 0], context.X[:, 1])
        engineered = np.column_stack([context.X, interaction])
        feature_names = list(context.feature_names or []) + ["interaction_feature_0_1"]
        context.X = engineered.astype(float)
        context.feature_names = feature_names
        context.metadata["engineered_features"] = 1
        self.logger.info("Added 1 engineered feature")
        return context
