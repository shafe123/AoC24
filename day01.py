import sys
from pathlib import Path
import re
from utilities import *

print(__name__)
filename = Path(sys.modules[__name__].__file__).name
pattern = re.compile(r'\d+')
match = pattern.search(filename)
day = match.group()

SAMPLE_TEXT = read_file(Path(f'./data/day{day}_sample.txt'))
TEXT = read_file(Path(f'./data/day{day}.txt'))

@separator('SAMPLE')
def print_sample():
    print(SAMPLE_TEXT)

@separator('ACTUAL')
def print_actual():
    print(TEXT)

print_sample()
print_actual()