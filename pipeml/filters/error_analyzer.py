from __future__ import annotations

import numpy as np
import pandas as pd

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class ErrorAnalyzer(BaseFilter):
    """Find misclassifications and summarize model weaknesses."""

    def __init__(self) -> None:
        super().__init__(name="ErrorAnalyzer")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.predictions is None or context.y_test is None:
            raise ValueError("Predictions and labels are required for error analysis")
        if context.probabilities is None:
            raise ValueError("Probability estimates are required for confidence scoring")

        errors = []
        for index, (true_label, predicted_label, probas) in enumerate(zip(context.y_test, context.predictions, context.probabilities)):
            confidence = float(np.max(probas))
            if true_label != predicted_label:
                errors.append(
                    {
                        "index": int(index),
                        "true_label": int(true_label),
                        "predicted_label": int(predicted_label),
                        "confidence": confidence,
                        "hardness": 1.0 - confidence,
                    }
                )

        if errors:
            errors_df = pd.DataFrame(errors).sort_values("hardness", ascending=False)
            hardest_samples = errors_df.head(5).to_dict(orient="records")
        else:
            hardest_samples = []

        per_class_accuracy = {}
        for label in np.unique(context.y_test):
            mask = context.y_test == label
            per_class_accuracy[str(int(label))] = float(np.mean(context.predictions[mask] == label))

        weakest_class = min(per_class_accuracy.items(), key=lambda item: item[1], default=("unknown", 0.0))
        weakness_summary = (
            f"The model struggled most with class {weakest_class[0]} "
            f"with accuracy {weakest_class[1]:.2f}."
        )

        context.error_rows = errors
        context.metadata["hardest_samples"] = hardest_samples
        context.metadata["weakness_summary"] = weakness_summary
        self.logger.info("Analyzed %s misclassifications", len(errors))
        return context
