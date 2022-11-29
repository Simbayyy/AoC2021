import os, pathlib, math

os.chdir(pathlib.Path(__file__).parent.resolve())

with open('input','r') as fp:
    data = fp.readlines()

totallines = len(data)

sumdata = [sum([int(data[i][j]) for i in range(totallines)]) for j in range(len(data[0])-1)]

gamma = int(''.join([str(round(i/totallines)) for i in sumdata]),2)
epsilon = int(''.join([str(1-abs(round(i/totallines))) for i in sumdata]),2)

print(gamma)
print(epsilon)
print(gamma*epsilon)
