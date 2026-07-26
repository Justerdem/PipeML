from __future__ import annotations

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Predictor(BaseFilter):
    """Generate predictions and probabilities for the test split."""

    def __init__(self) -> None:
        super().__init__(name="Predictor")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.model is None or context.X_test is None:
            raise ValueError("The model and test data must be available before predicting")
        if context.y_test is None:
            raise ValueError("Ground-truth labels are required for evaluation")

        predictions = context.model.predict(context.X_test)
        probabilities = context.model.predict_proba(context.X_test)
        context.predictions = predictions
        context.probabilities = probabilities
        self.logger.info("Generated predictions for %s samples", len(predictions))
        return context
