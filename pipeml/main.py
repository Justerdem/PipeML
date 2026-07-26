from __future__ import annotations

from pipeml.pipeline.orchestrator import PipelineOrchestrator


def main() -> None:
    orchestrator = PipelineOrchestrator()
    result = orchestrator.run()
    print("Pipeline completed successfully.")
    print(result["metrics"])


if __name__ == "__main__":
    main()
