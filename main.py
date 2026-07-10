from src.metrics.semantic_convergence import SemanticConvergence


def main():
    metric = SemanticConvergence()

    result = metric.compute([
        "Hello world.",
        "Hello world."
    ])

    print(result)


if __name__ == "__main__":
    main()