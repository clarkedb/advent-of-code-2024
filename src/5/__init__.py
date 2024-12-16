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

    corrected_invalid_middle_page_sum = 0
    corrected_updates = list()

    for update in updates:
        valid_update, modified = _validate_and_correct_update(update, rules)

        if modified:
            corrected_updates.append(valid_update)
            middle_page = valid_update[len(valid_update) // 2]
            corrected_invalid_middle_page_sum += int(middle_page)

    return corrected_invalid_middle_page_sum


def _validate_and_correct_update(
    update: list[str], rules: defaultdict[str, bool]
) -> tuple[list[str], bool]:
    valid_update = update.copy()
    modified = False

    n = len(valid_update)
    i = n - 1
    while i > 0:
        lowest_conflict_index = i
        for j in range(i - 1, -1, -1):
            if rules[f"{valid_update[i]}|{valid_update[j]}"]:
                lowest_conflict_index = j

        if lowest_conflict_index == i:
            i -= 1
            continue

        previous = valid_update.copy()
        valid_update.insert(lowest_conflict_index, previous[i])
        valid_update.pop(i + 1)
        modified = True

    return valid_update, modified
