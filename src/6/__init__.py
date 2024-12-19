from typing import TextIO


def part1(input: TextIO) -> int:
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
    visited = set()

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
    map = list()
    init_guard_cell = None
    for i, line in enumerate(input):
        row = list(line.strip())
        map.append(row)
        if init_guard_cell is not None:
            continue
        try:
            j = row.index("^")
            init_guard_cell = (j, i)
        except ValueError:
            continue

    if init_guard_cell is None:
        raise ValueError("no starting guard position detected")

    n = len(map)
    m = len(map[0])
    loop_obstructions = set()

    for i in range(n):
        for j in range(m):
            if map[i][j] != ".":
                # ignore guard or existing blocks
                continue

            direction = (0, -1)
            visited = set()
            guard_cell = init_guard_cell

            while True:
                x, y = guard_cell

                cell_state = (guard_cell, direction)
                if cell_state in visited:
                    loop_obstructions.add((j, i))
                    break

                visited.add(cell_state)

                x_prime, y_prime = x + direction[0], y + direction[1]
                if (x_prime < 0) or (y_prime < 0) or (x_prime >= m) or (y_prime >= n):
                    break

                if map[y_prime][x_prime] == "#" or (x_prime == j and y_prime == i):
                    # road block, must turn
                    direction = _turn_right(direction)
                else:
                    # advance
                    guard_cell = (x_prime, y_prime)

    return len(loop_obstructions)


def _turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    x, y = direction
    sign = -1 * int(x == 0)
    return (sign * y), x
