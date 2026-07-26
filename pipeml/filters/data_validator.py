from __future__ import annotations

import numpy as np

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataValidator(BaseFilter):
    """Validate data integrity before downstream processing."""

    def __init__(self) -> None:
        super().__init__(name="DataValidator")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X is None or context.y is None:
            raise ValueError("The context is missing X or y values")
        if context.X.shape[0] != context.y.shape[0]:
            raise ValueError("X and y contain a different number of samples")
        if context.X.size == 0:
            raise ValueError("No observations were found in the dataset")
        if not np.isfinite(context.X).all():
            raise ValueError("The feature matrix contains non-finite values")
        if np.unique(context.y).size < 2:
            raise ValueError("The target must contain at least two classes")

        context.metadata["validated"] = True
        self.logger.info("Validation passed for %s samples", context.X.shape[0])
        return context
