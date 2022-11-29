import os, pathlib
import pandas as pd

os.chdir(pathlib.Path(__file__).parent.resolve())

data = pd.read_csv('input', sep=" ")

aim = 0
horizontal = 0
vertical = 0

for index, row in data.iterrows():
    if row['direction'] == 'forward':
        horizontal += row['value']
        vertical += aim*row['value']
    if row['direction'] == 'up':
        aim -= row['value']
    if row['direction'] == 'down':
        aim += row['value']

print(horizontal*vertical)
