"""
CSI - Semantic Convergence Metric

First implementation using SentenceTransformers embeddings.
"""

from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.utils.helpers import validate_responses


class SemanticConvergence:
    """
    Compute semantic convergence among multiple LLM responses.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def compute(self, responses: List[str]) -> dict:
        """
        Compute semantic convergence.

        Parameters
        ----------
        responses : list[str]
            List of model responses.

        Returns
        -------
        dict
            Dictionary containing statistics and similarity matrix.
        """

        responses = validate_responses(responses)

        embeddings = self.model.encode(
            responses,
            convert_to_numpy=True
        )

        similarity_matrix = cosine_similarity(embeddings)

        mask = ~np.eye(len(similarity_matrix), dtype=bool)
        similarities = similarity_matrix[mask]

        return {
            "semantic_convergence": float(similarities.mean()),
            "mean_similarity": float(similarities.mean()),
            "std_similarity": float(similarities.std()),
            "min_similarity": float(similarities.min()),
            "max_similarity": float(similarities.max()),
            "responses": len(responses),
            "matrix": similarity_matrix.tolist()
        }