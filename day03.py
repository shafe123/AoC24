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
    ACTIVE_TEXT = "".join(ACTUAL)
    
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = mul_pattern.findall(ACTIVE_TEXT)
    return sum([int(match[0]) * int(match[1]) for match in matches])

def part2():
    ACTIVE_TEXT = "".join(ACTUAL)
    

    # find all dos...dont (and first and last)
    dos_pattern = re.compile(r"(?:^|do\(\))(.*?)(?=(?:don't\(\))|$)")
    all_matches = dos_pattern.findall(ACTIVE_TEXT)
    final = "".join(all_matches)

    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = mul_pattern.findall(final)
    return sum([int(match[0]) * int(match[1]) for match in matches])

print(part2())