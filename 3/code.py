import os, pathlib
import pandas as pd

os.chdir(pathlib.Path(__file__).parent.resolve())

data = pd.read_csv('input', sep=" ")

forward = data[data['direction'] == 'forward']

up = data[data['direction'] == 'up']
down = data[data['direction'] == 'down']

print(sum(forward['value'])*(-sum(up['value'])+sum(down['value'])))