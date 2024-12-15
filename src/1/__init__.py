from typing import TextIO
from collections import defaultdict


def part1(input: TextIO) -> int:
    l1 = list()
    l2 = list()
    for line in input:
        left, right = line.strip().split("   ")
        l1.append(int(left))
        l2.append(int(right))

    l1.sort()
    l2.sort()

    diff_sum = 0
    for n1, n2 in zip(l1, l2):
        diff_sum += abs(n1 - n2)

    return diff_sum


def part2(input: TextIO) -> int:
    l1 = defaultdict(int)
    l2 = defaultdict(int)
    for line in input:
        left, right = line.strip().split("   ")
        l1[left] += 1
        l2[right] += 1

    similarity_score = 0
    for number, left_count in l1.items():
        right_count = l2[number]
        incremental_similarity = int(number) * left_count * right_count
        similarity_score += incremental_similarity

    return similarity_score
