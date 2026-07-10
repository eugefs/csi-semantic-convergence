"""
Utility functions for the CSI project.
"""

from typing import Iterable


def validate_responses(responses: Iterable[str]) -> list[str]:
    """Validate and normalize model responses."""

    cleaned = [
        r.strip()
        for r in responses
        if isinstance(r, str) and r.strip()
    ]

    if len(cleaned) < 2:
        raise ValueError(
            "At least two non-empty responses are required."
        )

    return cleaned