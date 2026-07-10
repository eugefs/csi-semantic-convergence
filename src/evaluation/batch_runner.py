"""
Batch execution utilities for CSI experiments.
"""

from pathlib import Path

from src.utils.config import load_config


def find_experiments(root: str = "experiments") -> list[Path]:
    root = Path(root)
    return sorted(root.glob("*/config/config.yaml"))


def load_all_configs(root: str = "experiments") -> list[dict]:
    """Load every experiment configuration."""

    configs = []

    for config_path in find_experiments(root):
        config = load_config(str(config_path))
        configs.append(config)

    return configs