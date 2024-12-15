from typing import TextIO
import re


def part1(input: TextIO) -> int:
    product_sum = 0

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    instructions = input.read()

    matches = re.finditer(pattern, instructions, re.MULTILINE)
    for match in matches:
        a, b = match.groups()
        product = int(a) * int(b)
        product_sum += product

    return product_sum


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 3 part 2 not implemented")
