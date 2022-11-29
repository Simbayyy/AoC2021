import os, pathlib, math

os.chdir(pathlib.Path(__file__).parent.resolve())

with open('input','r') as fp:
    data = fp.readlines()

totallines = len(data)

sumdata = [sum([int(data[i][j]) for i in range(totallines)]) for j in range(len(data[0])-1)]

gamma = int(''.join([str(round(i/totallines)) for i in sumdata]),2)
epsilon = int(''.join([str(1-abs(round(i/totallines))) for i in sumdata]),2)


def findO2CO2(boolean):
    index = 0
    data_to_process = data
    while index<=len(data[0])-1:
        data_buffer = []
        lendata = len(data_to_process)
        one_amount = sum(int(data_to_process[i][index]) for i in range(lendata))
        if boolean:
            if one_amount*2 == lendata:
                significator =1
            else:
                significator =round(one_amount/lendata)
        else:
            if one_amount*2 == lendata:
                significator =0
            else:
                significator =abs(1-round(one_amount/lendata))
        for line in data_to_process:
            if line[index] == str(significator):
                data_buffer.append(line)
        if len(data_buffer) == 1:
            return data_buffer[0]
        data_to_process = data_buffer
        index+=1

print(findO2CO2(epsilon))
print(int(findO2CO2(epsilon),2))

print(int(findO2CO2(True)[:-1],2)*int(findO2CO2(False)[:-1],2))