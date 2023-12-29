import numpy as np

with open("input.txt") as f:
    data = f.read().split("\n")
    f.close()

rocks = np.empty((len(data), len(data[0])), dtype = str)
for i in range(len(data)):
    for j in range(len(data[0])):
        rocks[i,j] = data[i][j]

for offset in range(1, rocks.shape[0]):
    for row in range(rocks.shape[0] - offset):
        selection = (rocks[row, :] == ".") & (rocks[row + 1, :] == "O")
        rocks[row, selection] = "O"
        rocks[row + 1, selection] = "."

rows = len(rocks)

load = sum([sum(rocks[x,:] == "O")*(rows-x) for x in range(len(rocks))])
print("Solution to Day 14 - part 1:", load)

test = np.array([[1,2],[3,4]])