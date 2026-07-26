from __future__ import annotations

from pipeml.core.models import PipelineContext


class PipelineOrchestrator:
    """Coordinate the overall machine learning workflow."""

    def __init__(self) -> None:
        self.context = PipelineContext(dataset_name="breast_cancer")

    def run(self) -> dict[str, object]:
        raise NotImplementedError
