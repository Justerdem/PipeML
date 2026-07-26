from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from pipeml.core.models import PipelineContext
from pipeml.filters.base import BaseFilter
from pipeml.utils.plotting import save_confusion_matrix, save_feature_importance, save_roc_curve


class ReportGenerator(BaseFilter):
    """Write evaluation artifacts to disk."""

    def __init__(self, output_dir: str | Path | None = None) -> None:
        super().__init__(name="ReportGenerator")
        self.output_dir = Path(output_dir or "outputs")

    def run(self, context: PipelineContext) -> PipelineContext:
        self.output_dir.mkdir(parents=True, exist_ok=True)

        classification_report_path = self.output_dir / "classification_report.txt"
        metrics_path = self.output_dir / "metrics.json"
        confusion_path = self.output_dir / "confusion_matrix.png"
        roc_path = self.output_dir / "roc_curve.png"
        feature_importance_path = self.output_dir / "feature_importance.png"
        error_analysis_path = self.output_dir / "error_analysis.csv"

        classification_report_path.write_text(context.classification_report, encoding="utf-8")
        metrics_payload = dict(context.metrics)
        metrics_payload["cross_val_score"] = context.cross_val_score
        metrics_payload["weakness_summary"] = context.metadata.get("weakness_summary", "")
        metrics_path.write_text(json.dumps(metrics_payload, indent=2), encoding="utf-8")

        if context.confusion_matrix is not None:
            save_confusion_matrix(confusion_path, context.confusion_matrix)
        if context.probabilities is not None and context.y_test is not None:
            save_roc_curve(roc_path, context.y_test, context.probabilities)
        if context.model is not None and context.feature_names is not None:
            save_feature_importance(feature_importance_path, context.model, context.feature_names)

        errors_df = pd.DataFrame(context.error_rows)
        errors_df.to_csv(error_analysis_path, index=False)

        context.metadata["report_paths"] = {
            "classification_report": str(classification_report_path),
            "metrics_json": str(metrics_path),
            "confusion_matrix_png": str(confusion_path),
            "roc_curve_png": str(roc_path),
            "feature_importance_png": str(feature_importance_path),
            "error_analysis_csv": str(error_analysis_path),
        }
        return context
