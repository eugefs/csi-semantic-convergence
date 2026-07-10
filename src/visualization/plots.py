from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_similarity_matrix(matrix, output_file):
    """Save a heatmap of the similarity matrix."""

    matrix = np.array(matrix)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matrix,
        annot=True,
        cmap="viridis",
        square=True,
        vmin=0,
        vmax=1
    )

    plt.title("Semantic Similarity Matrix")
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()