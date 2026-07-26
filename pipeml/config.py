from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    raise NotImplementedError


def configure_logging(level: str = "INFO") -> None:
    raise NotImplementedError
