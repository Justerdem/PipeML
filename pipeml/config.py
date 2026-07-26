from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    if config_path is None:
        config_path = Path(__file__).resolve().parents[1] / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
