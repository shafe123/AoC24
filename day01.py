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

    col1, col2 = [], []
    for row in ACTIVE_TEXT:
        val1, val2 = [int(x) for x in row.split()]
        col1.append(val1)
        col2.append(val2)

    col1.sort()
    col2.sort()


    result = sum([abs(val - col2[index]) for index, val in enumerate(col1)])
    print(result)