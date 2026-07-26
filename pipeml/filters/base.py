from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from pipeml.core.models import PipelineContext

logger = logging.getLogger(__name__)


class BaseFilter(ABC):
    """Base class for each pipe-and-filter stage."""

    def __init__(self, name: str | None = None) -> None:
        self.name = name or self.__class__.__name__
        self.logger = logger

    @abstractmethod
    def run(self, context: PipelineContext) -> PipelineContext:
        """Apply the filter to the pipeline context."""
