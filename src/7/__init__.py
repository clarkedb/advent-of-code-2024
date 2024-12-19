from typing import TextIO
from itertools import product


def part1(input: TextIO) -> int:
    total = 0

    for line in input:
        test_value_str, operands_str = line.strip().split(": ")
        test_value = int(test_value_str)
        operands = list(map(int, operands_str.split(" ")))

        if _can_calculate_target(test_value, operands, ["+", "*"]):
            total += test_value

    return total


def part2(input: TextIO) -> int:
    total = 0

    for line in input:
        test_value_str, operands_str = line.strip().split(": ")
        test_value = int(test_value_str)
        operands = list(map(int, operands_str.split(" ")))

        if _can_calculate_target(test_value, operands, ["+", "*", "||"]):
            total += test_value

    return total


def _evaluate_expression(operands, operators):
    result = operands[0]

    for i, op in enumerate(operators):
        match op:
            case "+":
                result += operands[i + 1]
            case "*":
                result *= operands[i + 1]
            case "||":
                result = int(str(result) + str(operands[i + 1]))
            case _:
                raise ArithmeticError

    return result


def _can_calculate_target(test_value, operands, operators):
    n = len(operands) - 1
    operator_combinations = product(operators, repeat=n)

    for operators in operator_combinations:
        if _evaluate_expression(operands, operators) == test_value:
            return True

    return False
