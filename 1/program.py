import pathlib, os
import numpy as np

os.chdir(pathlib.Path(__file__).parent.resolve())



with open('input','r') as fp:
    values = np.genfromtxt(fp)

count = 0
for index in range(1,len(values)):
    if values[index] >= values[index-1]:
        count += 1

with open('output.txt','w') as fp:
    fp.write(str(count))