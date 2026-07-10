"""
Main entry point for the CSI framework.
"""

import json
from pathlib import Path

from src.evaluation.batch_runner import load_all_configs
from src.evaluation.evaluate import save_results
from src.metrics.semantic_convergence import SemanticConvergence


def main():
    configs = load_all_configs()

    print(f"\nRunning {len(configs)} experiment(s)\n")

    for config in configs:

        experiment = config["experiment"]["name"]

        print("=" * 60)
        print(f"Experiment: {experiment}")
        print("=" * 60)

        # Load responses
        with open(
            config["input"]["responses"],
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        responses = data["responses"]

        # Run every embedding model
        for model_name in config["models"]:

            print(f"\nModel: {model_name}")

            metric = SemanticConvergence(model_name)

            result = metric.compute(responses)

            # Create output directory
            output_dir = (
                Path("experiments")
                / experiment
                / "results"
                / model_name
            )

            output_dir.mkdir(parents=True, exist_ok=True)

            # Save results
            save_results(
                result,
                output_dir / "results.json",
            )

            print(
                f"Semantic convergence: "
                f"{result['semantic_convergence']:.3f}"
            )

            print(
                f"Results saved to: "
                f"{output_dir / 'results.json'}"
            )

        print()

    print("=" * 60)
    print("All experiments completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()