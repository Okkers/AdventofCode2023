import numpy as np

def symmetry_count(arr):
    checks = np.array([(arr[:,x] == arr[:,x+1]) for x in range(arr.shape[1]-1)])
    syms = []
    for i in checks:
        if len(i[i==False]) > 1:
            syms.append(False)
        else:
            syms.append(True)

    symmetry = np.argwhere(checks == 1)
    for sym_point in symmetry:
        sym_point = sym_point[0]
        extend = [(arr[:,sym_point-i] == arr[:,sym_point+i+1]) for i in range(min(arr.shape[1]-sym_point-1, sym_point+1))]
        smudge = sum([len(x[x==False]) for x in extend]) == 1
        if smudge:
            return sym_point+1,True
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

print(sym_count)