"""
Batch execution utilities for CSI experiments.
"""

from pathlib import Path


def find_experiments(root: str = "experiments") -> list[Path]:
    """
    Find all experiment configuration files.

    Returns
    -------
    list[Path]
        Paths to every config.yaml file.
    """
    root = Path(root)

    return sorted(root.glob("*/config/config.yaml"))