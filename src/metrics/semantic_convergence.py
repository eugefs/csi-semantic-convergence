"""
CSI - Semantic Convergence Metric

Author: Eugenio Fontenla Suárez
Project: CSI - Continuum Semantic Index
"""

from typing import List


class SemanticConvergence:
    """Base class for CSI semantic convergence metrics."""

    def __init__(self):
        pass

    def compute(self, responses: List[str]):
        """Compute semantic convergence.

        Parameters
        ----------
        responses : list[str]
            Model responses to compare.

        Returns
        -------
        dict
            Placeholder for future metric outputs.
        """
        return {
            "status": "not_implemented",
            "n_responses": len(responses)
        }