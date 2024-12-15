import argparse
import importlib
import sys
from time import time


def main():
    parser = argparse.ArgumentParser(description="Advent of Code CLI")
    parser.add_argument(
        "--day",
        type=int,
        choices=range(1, 26),
        required=True,
        help="Day of the challenge (1-25)",
    )
    parser.add_argument(
        "--part",
        type=int,
        choices=[1, 2],
        required=True,
        help="Part of the challenge (1 or 2)",
    )
    parser.add_argument(
        "--input",
        type=argparse.FileType("r"),
        required=True,
        help="Input file for the challenge",
    )

    args = parser.parse_args()

    day = args.day
    part = args.part
    input_file = args.input

    try:
        module_name = f"{day}"
        module = importlib.import_module(module_name)

        function_name = f"part{part}"
        challenge_function = getattr(module, function_name)

        start = time()
        result = challenge_function(input_file)
        duration_ms = 1000 * (time() - start)

        print(f"day {day} - part {part} [completed in {duration_ms:.4f} ms]")
        print(f">> {result}")

    except ModuleNotFoundError:
        print(f"Error: Module for Day {day} not found.", file=sys.stderr)
    except AttributeError:
        print(f"Error: Function for Day {day}, Part {part} not found.", file=sys.stderr)


if __name__ == "__main__":
    main()
