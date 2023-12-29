import numpy as np

def symmetry_count(arr):
    checks = np.array([np.all(arr[:,x] == arr[:,x+1]) for x in range(arr.shape[1]-1)])
    symmetry = np.argwhere(checks == 1)
    
    for sym_point in symmetry:
        sym_point = sym_point[0]
        extend = [np.all(arr[:,sym_point-i] == arr[:,sym_point+i+1]) for i in range(min(arr.shape[1]-sym_point-1, sym_point+1))]
        if False not in extend:
            return sym_point+1, True
    return 0, False

with open("input.txt") as f:
    data = f.read().split("\n\n")
    f.close()

sym_count = 0
for mirror in data:
    mirror = mirror.split("\n")
    arr = np.empty((len(mirror), len(mirror[0])), dtype=str)

    for i in range(len(mirror)):
        for j in range(len(mirror[0])):
            arr[i,j] = mirror[i][j]
    arr_rows = arr.T

    cols, valid_col = symmetry_count(arr)
    rows, valid_row = symmetry_count(arr_rows)
    if valid_row:
        sym_count += rows*100
    elif valid_col:
        sym_count += cols

print("Solution to Day 13 - part 1:", sym_count)