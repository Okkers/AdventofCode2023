import numpy as np 
from tqdm import tqdm
arr = np.genfromtxt("input.txt", dtype=bytes, comments=None, delimiter=1).astype(str)

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

def beam_search(arr, init_pos, init_dir):
    beamed_arr = np.full((arr.shape), ".")
    queue = []
    init_dir = refract(arr, init_pos, init_dir)
    for dir in init_dir:
        queue.append([init_pos, dir])

    visited = []
    while len(queue) != 0:
        beam_pos, beam_dir = queue.pop(0)
        beamed_arr[beam_pos] = "#"

        new_pos = tuple([sum(x) for x in zip(beam_pos, beam_dir)])
        key = hash((new_pos, beam_dir))

        if key not in visited:
            visited.append(key)

            if within_bounds(arr, new_pos):
                new_dirs = refract(arr, new_pos, beam_dir)

                for direction in new_dirs:
                    queue.append([new_pos, direction])

init_poss_upper = [((0,x),(1,0)) for x in range(1, arr.shape[1]-1)]
init_poss_lower = [((arr.shape[0]-1, x), (-1,0)) for x in range(1,arr.shape[1]-1)]
init_poss_left = [((x,0), (0,1)) for x in range(1, arr.shape[0]-1)]
init_poss_right = [((x,arr.shape[1]-1), (0,-1)) for x in range(1, arr.shape[0]-1)]
init_poss_corners = [((0,0), (0,1)), ((0,0), (1,0)), 
                     ((arr.shape[0]-1, 0), (-1,0)), ((arr.shape[0]-1,0), (0,1)),
                     ((0, arr.shape[1]-1), (1,0)), ((0, arr.shape[1]-1), (0,-1)),
                     ((arr.shape[0]-1, arr.shape[1]-1), (-1,0)), ((arr.shape[0]-1, arr.shape[1]-1), (0,-1))]
init_poss = init_poss_upper + init_poss_lower + init_poss_left + init_poss_right + init_poss_corners

lit_tiles = []
for init_pos, init_dir in tqdm(init_poss):
    beam_arr = np.full((arr.shape), ".")

ans = beam_search(arr, (1,0), (0,1))
print("Solution to Day 16 - part 2:", np.max(lit_tiles))