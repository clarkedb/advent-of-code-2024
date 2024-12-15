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
    product_sum = 0

    pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    instructions = input.read()
    enabled = True

    matches = re.finditer(pattern, instructions, re.MULTILINE)
    for match in matches:
        a, b, do, dont = match.groups()[1:]
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            product = int(a) * int(b)
            product_sum += product

    return product_sum
