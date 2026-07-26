from __future__ import annotations

from abc import ABC, abstractmethod

from pipeml.core.models import PipelineContext


class BaseFilter(ABC):
    """Base class for every filter in the pipeline."""

    def __init__(self, name: str | None = None) -> None:
        self.name = name or self.__class__.__name__

    @abstractmethod
    def run(self, context: PipelineContext) -> PipelineContext:
        raise NotImplementedError
