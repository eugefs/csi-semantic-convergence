from src.utils.helpers import validate_responses


def main():

    responses = [
        "Hello world.",
        "Hello world.",
        ""
    ]

    cleaned = validate_responses(responses)

    print(cleaned)


if __name__ == "__main__":
    main()