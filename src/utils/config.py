"""
Configuration utilities for CSI.
"""

from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    """
    Load a YAML configuration file.
    """
    with open(Path(path), "r", encoding="utf-8") as file:
        return yaml.safe_load(file)