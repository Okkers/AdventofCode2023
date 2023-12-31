import numpy as np 

arr = np.genfromtxt("input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)
beamed_arr = arr.copy()

def within_bounds(arr, ind):
    if ind[0] >= 0 and ind[0] < arr.shape[0] and ind[1] >= 0 and ind[1] < arr.shape[1]:
        return True
    return False

def refract(arr, ind, dir):
    if arr[ind] == "|":
        if dir == (0, 1) or dir == (0, -1):
            return (1,0), (-1,0)
        return [dir]
        
    if arr[ind] == "-":
        if dir == (1,0) or dir == (-1,0):
            return (0,-1), (0,1)
        return [dir]

    if arr[ind] == "/":
        return [(-dir[1], -dir[0])]
    
    if arr[ind] == '\\':
        return [(dir[1], dir[0])]
    
    if arr[ind] in [".", "#"]:
        return [dir]

beams = []
init_pos = (0,0)
init_dir = refract(arr, init_pos, (0,1))
for dir in init_dir:
    beams.append([init_pos, dir])

visited = []
while len(beams) != 0:
    beam_pos, beam_dir = beams.pop(0)
    beamed_arr[beam_pos] = "#"

    new_pos = tuple([sum(x) for x in zip(beam_pos, beam_dir)])
    key = hash((new_pos, beam_dir))

    if key not in visited:
        visited.append(key)

        if within_bounds(arr, new_pos):
            new_dirs = refract(arr, new_pos, beam_dir)

            for direction in new_dirs:
                beams.append([new_pos, direction])

print("Solution to Day 16 - part 1:", np.count_nonzero(beamed_arr == "#"))