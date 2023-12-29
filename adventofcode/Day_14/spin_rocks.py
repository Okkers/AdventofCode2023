import numpy as np

with open("input.txt") as f:
    data = f.read().split("\n")
    f.close()

rocks = np.genfromtxt("input.txt", dtype = bytes, comments=None, delimiter=1).astype(str)

def lever(arr):
    for offset in range(1, arr.shape[0]):
        for row in range(arr.shape[0] - offset):
            selection = (arr[row, :] == ".") & (arr[row + 1, :] == "O")
            arr[row, selection] = "O"
            arr[row + 1, selection] = "."
    return arr

def spin_cycle(arr):
    for dir in [0, 3, 2, 1]:
        arr = np.rot90(arr, dir)
        arr = lever(arr)
        arr = np.rot90(arr, -dir)
    return arr

seen_arrs = {}
cycles = 0
itrs = 0
found = False
while cycles < 10**9:
    rocks = spin_cycle(rocks)

    if not found:
        key = hash(rocks.data.tobytes())
        if key in seen_arrs:
            found = True
            cycles = 10**9 - (10**9 - cycles) % (cycles-seen_arrs[key])
        else:
            seen_arrs[key] = cycles
    cycles += 1

rows = len(rocks)

load = sum([sum(rocks[x,:] == "O")*(rows-x) for x in range(len(rocks))])
print("Solution to Day 14 - part 2:", load)