import sys
from pathlib import Path
import re
from utilities import *

filename = Path(sys.modules[__name__].__file__).name
pattern = re.compile(r'\d+')
match = pattern.search(filename)
day = match.group()

SAMPLE_TEXT = read_file(Path(f'./data/day{day}_sample.txt'))
TEXT = read_file(Path(f'./data/day{day}.txt'))

def part1():
    ACTIVE_TEXT = TEXT

    safe_rows = []
    for row in ACTIVE_TEXT:
        vals = [int(x) for x in row.split()]

        # ascending check
        if all([0 < y - x < 4 for x, y in zip(vals[::], vals[1::])]):
            safe_rows.append(vals)
            continue

        # descending check
        if all([0 < x - y < 4 for x, y in zip(vals[::], vals[1::])]):
            safe_rows.append(vals)
            continue

    return len(safe_rows)

def part2():
    ACTIVE_TEXT = TEXT

    safe_rows = []
    for row in ACTIVE_TEXT:
        vals = [int(x) for x in row.split()]

        # ascending check
        if all([0 < y - x < 4 for x, y in zip(vals[::], vals[1::])]):
            safe_rows.append(vals)
            continue

        # descending check
        if all([0 < x - y < 4 for x, y in zip(vals[::], vals[1::])]):
            safe_rows.append(vals)
            continue

        for index, _ in enumerate(vals):
            copy = vals[::]
            copy.pop(index)

            # ascending check
            if all([0 < y - x < 4 for x, y in zip(copy[::], copy[1::])]):
                safe_rows.append(vals)
                break

            # descending check
            if all([0 < x - y < 4 for x, y in zip(copy[::], copy[1::])]):
                safe_rows.append(vals)
                break

    return len(safe_rows)

print(part2())