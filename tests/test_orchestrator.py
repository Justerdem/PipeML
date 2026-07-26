from pathlib import Path

from pipeml.pipeline.orchestrator import PipelineOrchestrator


def test_pipeline_orchestrator_generates_reports(tmp_path):
    orchestrator = PipelineOrchestrator(output_dir=tmp_path, dataset_name="breast_cancer")
    result = orchestrator.run()

    assert result["metrics"]["accuracy"] >= 0.0
    assert result["report_paths"]["classification_report"] is not None
    assert Path(result["report_paths"]["classification_report"]).exists()
    assert Path(result["report_paths"]["metrics_json"]).exists()
    assert Path(result["report_paths"]["confusion_matrix_png"]).exists()
    assert Path(result["report_paths"]["roc_curve_png"]).exists()
    assert Path(result["report_paths"]["error_analysis_csv"]).exists()
