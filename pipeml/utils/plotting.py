from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve


def save_confusion_matrix(output_path: Path, confusion_matrix: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.imshow(confusion_matrix, cmap="Blues")
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    for row_index in range(confusion_matrix.shape[0]):
        for col_index in range(confusion_matrix.shape[1]):
            ax.text(col_index, row_index, int(confusion_matrix[row_index, col_index]), ha="center", va="center")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def save_roc_curve(output_path: Path, y_true: np.ndarray, probabilities: np.ndarray) -> None:
    if probabilities.shape[1] > 1:
        positive_class = 1
        y_score = probabilities[:, positive_class]
    else:
        y_score = probabilities[:, 0]
    fpr, tpr, _ = roc_curve(y_true, y_score)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(fpr, tpr, label="ROC Curve")
    ax.plot([0, 1], [0, 1], linestyle="--", color="gray")
    ax.set_title("ROC Curve")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def save_feature_importance(output_path: Path, model: Any, feature_names: list[str]) -> None:
    importances = getattr(model, "feature_importances_", None)
    if importances is None:
        return

    indices = np.argsort(importances)[::-1]
    ordered_features = [feature_names[index] for index in indices]
    ordered_importances = importances[indices]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh(ordered_features, ordered_importances)
    ax.set_title("Feature Importance")
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
