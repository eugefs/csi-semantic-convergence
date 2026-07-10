"""
CSI - Semantic Convergence Metric
"""

from typing import List

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from src.utils.helpers import validate_responses


class SemanticConvergence:

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def compute(self, responses: List[str]) -> dict:

        responses = validate_responses(responses)

        embeddings = self.model.encode(responses)

        similarity_matrix = cosine_similarity(embeddings)

        mask = ~np.eye(len(similarity_matrix), dtype=bool)

        score = similarity_matrix[mask].mean()

        return {
            "semantic_convergence": float(score),
            "responses": len(responses),
            "matrix": similarity_matrix.tolist()
        }