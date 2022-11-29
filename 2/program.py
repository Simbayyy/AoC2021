import pathlib, os
import numpy as np

os.chdir(pathlib.Path(__file__).parent.resolve())



with open('input','r') as fp:
    values = np.genfromtxt(fp)

sliding_values = np.array([values[i] + values[i-1] + values [i-2] for i in range(2,len(values))])

count = 0
for index in range(1,len(sliding_values)):
    if sliding_values[index] > sliding_values[index-1]:
        count += 1

with open('output.txt','w') as fp:
    fp.write(str(count))