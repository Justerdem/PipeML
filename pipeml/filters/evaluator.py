from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class Evaluator(BaseFilter):
    """Compute standard metrics for the trained classifier."""

    def __init__(self) -> None:
        super().__init__(name="Evaluator")

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.predictions is None or context.y_test is None:
            raise ValueError("Predictions and ground-truth labels are required for evaluation")

        context.confusion_matrix = confusion_matrix(context.y_test, context.predictions)
        context.metrics = {
            "accuracy": float(accuracy_score(context.y_test, context.predictions)),
            "precision": float(precision_score(context.y_test, context.predictions, average="weighted")),
            "recall": float(recall_score(context.y_test, context.predictions, average="weighted")),
            "f1_score": float(f1_score(context.y_test, context.predictions, average="weighted")),
        }
        if context.probabilities is not None and context.probabilities.shape[1] > 1:
            positive_class = 1 if np.unique(context.y_test).size > 1 else 0
            context.roc_auc = float(roc_auc_score(context.y_test, context.probabilities[:, positive_class]))
            context.metrics["roc_auc"] = context.roc_auc
        context.classification_report = classification_report(context.y_test, context.predictions)
        self.logger.info("Evaluation completed with accuracy %.3f", context.metrics["accuracy"])
        return context
