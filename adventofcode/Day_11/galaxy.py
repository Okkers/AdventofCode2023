import numpy as np

def distance(gal1, gal2):
    return abs(gal1[0]-gal2[0]) + abs(gal1[1]-gal2[1])

with open("input.txt") as f:
    chart = f.read().split("\n")[:-1]

arr = np.full((len(chart), len(chart[0])), ".")
expanses_x = []
expanses_y = []

for i in range(len(chart)):
    for j in range(len(chart[0])):
        arr[i,j] = chart[i][j]
    if "#" not in chart[i]:
        expanses_x.append(i)
    checker = [chart[x][i] for x in range(len(chart))]
    if "#" not in checker:
        expanses_y.append(i)

gals= np.argwhere(arr == "#")
ans_1 = 0
ans_2 = 0
for ind in range(len(gals)):
    for j in range(ind+1, len(gals)):
        for row in range(min(gals[ind][0], gals[j][0]), max(gals[ind][0], gals[j][0])):
            ans_1 += 2 if row in expanses_x else 1
            ans_2 += 10**6 if row in expanses_x else 1
        for col in range(min(gals[ind][1], gals[j][1]), max(gals[ind][1], gals[j][1])):
            ans_1 += 2 if col in expanses_y else 1
            ans_2 += 10**6 if col in expanses_y else 1
print("Solution to Day 11 - part 1:", ans_1)
print("Solution to Day 12 - part 2:", ans_2)