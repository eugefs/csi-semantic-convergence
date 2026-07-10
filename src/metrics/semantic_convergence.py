"""
CSI - Semantic Convergence Metric
"""

from typing import List

from src.utils.helpers import validate_responses


class SemanticConvergence:
    """First implementation of the CSI metric."""

    def compute(self, responses: List[str]) -> dict:
        responses = validate_responses(responses)

        return {
            "n_responses": len(responses),
            "responses": responses,
            "status": "validated"
        }