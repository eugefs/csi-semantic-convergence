import json
from pathlib import Path


def save_results(results: dict, output_file: str):

    output = Path(output_file)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)