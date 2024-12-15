from typing import TextIO
from collections import defaultdict


def part1(input: TextIO) -> int:
    rules = defaultdict(bool)
    updates = list()
    all_rules_parsed = False
    for line in input:
        content = line.strip()
        if content == "":
            all_rules_parsed = True
            continue

        if not all_rules_parsed:
            rules[content] = True
        else:
            update_pages = content.split(",")
            updates.append(update_pages)

    valid_middle_page_sum = 0

    for update in updates:
        valid_update = True

        for i in range(len(update)):
            page = update[i]
            for subsequent_page in update[i:]:
                if rules[f"{subsequent_page}|{page}"]:
                    valid_update = False
                    break
            if not valid_update:
                break

        if valid_update:
            middle_page = update[len(update) // 2]
            valid_middle_page_sum += int(middle_page)

    return valid_middle_page_sum


def part2(input: TextIO) -> int:
    raise NotImplementedError("day 5 part 2 not implemented")
