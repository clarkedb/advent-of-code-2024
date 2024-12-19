from typing import TextIO


def part1(input: TextIO) -> int:
    visited = set()
    map = list()
    guard_cell = None
    for i, line in enumerate(input):
        row = list(line.strip())
        map.append(row)
        if guard_cell is not None:
            continue
        try:
            j = row.index("^")
            guard_cell = (j, i)
        except ValueError:
            continue

    if guard_cell is None:
        raise ValueError("no starting guard position detected")

    n = len(map)
    m = len(map[0])
    direction = (0, -1)

    while True:
        x, y = guard_cell
        if (x < 0) or (y < 0) or (x >= m) or (y >= n):
            break

        visited.add(guard_cell)

        x_prime, y_prime = x + direction[0], y + direction[1]

        if map[y_prime][x_prime] == "#":
            # road block, must turn
            direction = _turn_right(direction)
        else:
            # advance
            guard_cell = (x_prime, y_prime)

    return len(visited)


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 6 part 2 not implemented")


def _turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    x, y = direction
    sign = -1 * int(x == 0)
    return (sign * y), x
