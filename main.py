import json

from src.evaluation.batch_runner import load_all_configs
from src.metrics.semantic_convergence import SemanticConvergence


def main():

    configs = load_all_configs()

    print(f"Running {len(configs)} experiment(s)\n")

    for config in configs:

        print(f"Experiment: {config['experiment']['name']}")

        with open(
            config["input"]["responses"],
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        for model in config["models"]:

            print(f"  Model: {model}")

            metric = SemanticConvergence(model)

            result = metric.compute(data["responses"])

            print(
                f"    Semantic convergence: "
                f"{result['semantic_convergence']:.3f}"
            )


if __name__ == "__main__":
    main()