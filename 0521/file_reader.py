from pathlib import Path
import os

print(os.getcwd())

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
