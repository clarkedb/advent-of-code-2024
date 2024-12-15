from typing import TextIO


def part1(input: TextIO) -> int:
    safe_count = 0
    for line in input:
        levels = line.strip().split(" ")
        safe = _safe_levels(levels)
        if safe:
            safe_count += 1

    return safe_count


def part2(input: TextIO) -> int:
    safe_count = 0
    for line in input:
        levels = line.strip().split(" ")
        safe = _safe_levels(levels)
        if safe:
            safe_count += 1
            continue

        for i in range(len(levels)):
            restricted = levels[:i] + levels[i + 1 :]
            safe_restricted = _safe_levels(restricted)
            if safe_restricted:
                safe_count += 1
                break

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
