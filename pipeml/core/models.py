from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class PipelineContext:
    """Shared state passed between pipe-and-filter stages."""

    dataset_name: str
    X: np.ndarray | None = None
    y: np.ndarray | None = None
    feature_names: list[str] | None = None
    target_name: str | None = None
    X_train: np.ndarray | None = None
    X_test: np.ndarray | None = None
    y_train: np.ndarray | None = None
    y_test: np.ndarray | None = None
    predictions: np.ndarray | None = None
    probabilities: np.ndarray | None = None
    model: Any = None
    metrics: dict[str, float] = field(default_factory=dict)
    confusion_matrix: np.ndarray | None = None
    classification_report: str = ""
    roc_auc: float | None = None
    cross_val_score: float | None = None
    error_rows: list[dict[str, Any]] = field(default_factory=list)
    feature_importance: np.ndarray | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
