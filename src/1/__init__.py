from typing import TextIO


def part1(input: TextIO) -> int:
    l1 = list()
    l2 = list()
    for line in input:
        s1, s2 = line.strip().split("   ")
        l1.append(int(s1))
        l2.append(int(s2))

    l1.sort()
    l2.sort()

    diff_sum = 0
    for n1, n2 in zip(l1, l2):
        diff_sum += abs(n1 - n2)

    return diff_sum


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 1 part 2 not implemented")
