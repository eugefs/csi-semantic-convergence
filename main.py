from src.metrics.semantic_convergence import SemanticConvergence


def main():

    responses = [
        "Artificial intelligence is transforming science.",
        "AI is changing scientific research.",
        "Machine learning improves research workflows."
    ]

    metric = SemanticConvergence()

    result = metric.compute(responses)

    print(result)


if __name__ == "__main__":
    main()