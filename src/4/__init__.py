from typing import TextIO


def part1(input: TextIO) -> int:
    grid = list()
    for line in input:
        grid.append(list(line))

    count_xmas = 0

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            char = grid[i][j]
            if char != "X":
                continue

            hits = _search_for_xmas(grid, (i, j), (n, m))
            count_xmas += hits

    return count_xmas


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 4 part 2 not implemented")


def _search_for_xmas(
    grid: list[list[str]], coords: tuple[int, int], shape: tuple[int, int]
) -> int:
    found = _scan(list("XMAS"), grid, coords, shape)
    return found


def _scan(
    query: list[str],
    grid: list[list[str]],
    coords: tuple[int, int],
    shape: tuple[int, int],
    direction: int | None = None,
) -> int:
    if len(query) == 0:
        return 0

    x, y = coords
    if (x < 0) or (y < 0) or (x >= shape[0]) or (y >= shape[1]):
        # out of bounds
        return 0

    partial_query = query[0]
    current = grid[x][y]

    if current != partial_query:
        return 0

    # no need to search further
    if len(query) == 1:
        return 1

    ordinals = [0] * 8
    offsets = [(x, y) for y in [-1, 0, 1] for x in [-1, 0, 1] if (x, y) != (0, 0)]

    for i in range(8):
        if (direction is not None) and (direction != i):
            continue

        offset = offsets[i]
        new_coords = (x + offset[0], y + offset[1])
        res = _scan(query[1:], grid, new_coords, shape, direction=i)
        ordinals[i] = res

    return sum(ordinals)
