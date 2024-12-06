import sys
from pathlib import Path
import re
from utilities import *

filename = Path(sys.modules[__name__].__file__).name
pattern = re.compile(r'\d+')
match = pattern.search(filename)
day = match.group()

SAMPLE = read_file(Path(f'./data/day{day}_sample.txt'))
ACTUAL = read_file(Path(f'./data/day{day}.txt'))

def part1():
    ACTIVE_TEXT = [[char for char in line] for line in SAMPLE]
    grid = ACTIVE_TEXT
    search = [['X', 'M', 'A', 'S']]

    # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    vertical = list(zip(*search[::-1]))
    backwards = list(zip(*vertical[::-1]))
    upsidedown = list(zip(*backwards[::-1]))

    diagonal = [['X', None, None, None],
                [None, 'M', None, None],
                [None, None, 'A', None],
                [None, None, None, 'S']
                ]
    diagonal_right = list(zip(*diagonal[::-1]))
    diagonal_down = list(zip(*diagonal_right[::-1]))
    diagonal_last = list(zip(*diagonal_down[::-1]))

    patterns = [search, vertical, backwards, upsidedown, diagonal, diagonal_right, diagonal_down, diagonal_last]

    count = 0
    for row, vals in enumerate(grid):
        for col, _ in enumerate(vals):
            for pattern in patterns:
                if check_match(grid, row, col, pattern):
                    count += 1
    return count
    
def check_match(grid: list[list[str]], row_offset: int, col_offset: int, pattern: list[list[str]]):
    for row, text in enumerate(pattern):
        if row_offset + row >= len(grid):
            return False

        for col, val in enumerate(text):
            if col_offset + col >= len(grid[0]):
                return False

            if val is None:
                continue

            if grid[row_offset + row][col_offset + col] != val:
                return False
    return True

print(part1())