import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data1 = df["math score"].tolist()
data2 = df["reading score"].tolist()
data3 = df["writing score"].tolist()

data = []

row = 0

for i in data1:
    k = int(data1[row]) + int(data2[row]) + int(data3[row])
    data.append(k)
    row = row + 1

print(data)

mean = statistics.mean(data)

sd = statistics.stdev(data)

range1h_min, range1h_max = mean - sd, mean + sd
range2h_min, range2h_max = mean - 2*sd, mean + 2*sd
range3h_min, range3h_max = mean - 3*sd, mean + 3*sd

#range1h = []
#for i in data:
    #if i > range1h_min and i < range1h_max:
        #range1h.append(i)

#One line code from the above for loop
range1h = [i for i in data if i > range1h_min and i < range1h_max]  
range2h = [i for i in data if i > range2h_min and i < range2h_max]
range3h = [i for i in data if i > range3h_min and i < range3h_max]

range1length = len(range1h)
range2length = len(range2h)
range3length = len(range3h)

datalength = len(data)

range1_percentage = (range1length/datalength) * 100
range2_percentage = (range2length/datalength) * 100
range3_percentage = (range3length/datalength) * 100

print("Range 1 percentage = " + str(range1_percentage), ", Range 2 percentage = " + str(range2_percentage),", Range 3 percentage = " + str(range3_percentage))