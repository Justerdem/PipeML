from __future__ import annotations

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter


class ModelTrainer(BaseFilter):
    """Train the classification model."""

    def __init__(self, model_name: str = "random_forest") -> None:
        super().__init__(name="ModelTrainer")
        self.model_name = model_name

    def run(self, context: PipelineContext) -> PipelineContext:
        if context.X_train is None or context.y_train is None:
            raise ValueError("The context must contain training data before fitting")

        if self.model_name == "random_forest":
            model = RandomForestClassifier(n_estimators=120, random_state=42, class_weight="balanced")
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")

        model.fit(context.X_train, context.y_train)
        scores = cross_val_score(model, context.X_train, context.y_train, cv=5, scoring="accuracy")
        context.model = model
        context.cross_val_score = float(scores.mean())
        context.metadata["model_name"] = self.model_name
        self.logger.info("Model trained with mean cross-validation accuracy %.3f", context.cross_val_score)
        return context
