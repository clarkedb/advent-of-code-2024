from typing import TextIO


def part1(input: TextIO) -> int:
    safe_count = 0
    for line in input:
        levels = line.strip().split(" ")
        safe = _safe_levels(levels)
        if safe:
            safe_count += 1

    return safe_count


def _safe_levels(levels: list[str]) -> bool:
    direction = int(levels[1]) > int(levels[0])
    for i in range(1, len(levels)):
        curr = int(levels[i])
        prev = int(levels[i - 1])

        step_direction = curr > prev
        if direction != step_direction:
            return False

        diff = abs(curr - prev)
        if diff < 1 or diff > 3:
            return False

    return True


def part2(input: TextIO) -> str:
    raise NotImplementedError("day 2 part 2 not implemented")
