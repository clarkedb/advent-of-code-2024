from typing import TextIO
from collections import defaultdict
from itertools import combinations


def part1(input: TextIO) -> int:
    n = 50
    antenna_by_type: dict[str, list[tuple[int, int]]] = defaultdict(
        list[tuple[int, int]]
    )

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == ".":
                continue

            antenna_by_type[char].append((x, y))

    antinodes = set()

    valid_coordinates = lambda p: all([c >= 0 and c < n for c in p])

    for k, antenna in antenna_by_type.items():
        for node1, node2 in combinations(antenna, 2):
            delta_x = node1[0] - node2[0]
            delta_y = node1[1] - node2[1]

            antinode1 = (node1[0] + delta_x, node1[1] + delta_y)
            if valid_coordinates(antinode1):
                antinodes.add(antinode1)

            antinode2 = (node2[0] - delta_x, node2[1] - delta_y)
            if valid_coordinates(antinode2):
                antinodes.add(antinode2)

    return len(antinodes)


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 8 part 2 not implemented")
