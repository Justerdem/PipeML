from __future__ import annotations

import numpy as np
import pandas as pd

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class DataCleaner(BaseFilter):
    """Clean the feature matrix by removing invalid values and standardizing shape."""

    def __init__(self) -> None:
        super().__init__(name="DataCleaner")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X is None:
            raise ValueError("The dataset has not been loaded")

        frame = pd.DataFrame(context.X, columns=context.feature_names or [f"feature_{index}" for index in range(context.X.shape[1])])
        frame = frame.apply(pd.to_numeric, errors="coerce")
        frame = frame.dropna(axis=1, how="all")
        frame = frame.fillna(frame.median())

        context.X = frame.to_numpy(dtype=float)
        context.y = np.asarray(context.y).reshape(-1)
        context.metadata["cleaned_rows"] = int(context.X.shape[0])
        self.logger.info("Cleaning completed; %s rows remain", context.X.shape[0])
        return context
