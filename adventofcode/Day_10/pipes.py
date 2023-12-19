import numpy as np
from helper import follow_pipe, within_bounds

with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

pipes = np.full((len(data[0]), len(data)), ".")
for x in range(len(data)):
    for y in range(len(data[0])):
        pipes[x,y] = data[x][y]

def constraints(arr, new_ind, adj_ind, init = False):
    if init:
        if ((arr[new_ind] == "|" and adj_ind[1] == 0) or (arr[new_ind] == "-" and adj_ind[0] == 0) or
            (arr[new_ind] == "L" and (adj_ind in [(1,0), (0,-1)])) or 
            (arr[new_ind] == "J" and (adj_ind in [(1,0), (0,1)]))  or
            (arr[new_ind] == "7" and (adj_ind in [(0,1), (-1,0)])) or
            (arr[new_ind] == "F") and (adj_ind in [(-1,0), (0,-1)])):
            return True 
        return False
    else:
        if arr[new_ind] not in ["S", "."] and new_ind == adj_ind:
            return True
        return False

adjs = [(-1,0), (0,1), (1,0), (0,-1)]
start = [x[0] for x in np.where(pipes == "S")]
visited = [start]
front = start
dir = []

#Initialization
found = False
for adj_x, adj_y in adjs:
    new_x = start[0] + adj_x
    new_y = start[1] + adj_y
    if not found:
        if within_bounds(pipes, (new_x, new_y)):
            if constraints(pipes, (new_x, new_y), (adj_x, adj_y), init=True):
                front = (new_x,new_y)
                dir = follow_pipe(pipes, (new_x, new_y), (adj_x, adj_y))
                found = True

cnt = 1
while front != start:
    if front in visited:
        front = start
    else:
        visited.append(front)
        next = False
        for adj_x, adj_y in adjs:
            new_x = front[0] + adj_x
            new_y = front[1] + adj_y
            dir_x = dir[0]
            dir_y = dir[1]
            if within_bounds(pipes, (new_x, new_y)) and [new_x, new_y] not in visited:
                if pipes[new_x, new_y] in ["|", "-", "L", "J", "7", "F"] and [dir_x, dir_y] == [adj_x, adj_y]:
                    front = (new_x,new_y)
                    dir = follow_pipe(pipes, (new_x, new_y), dir)
                    cnt += 1
                    next = True
            if next:
                break

print("Solution to Day 10 - part 1:", int(np.ceil(cnt/2)))

# Shoelace + Pick's
area = sum(x1*y2-x2*y1 for (x1,y1), (x2,y2) in zip([*visited, visited[0]], [*visited, visited[0]][1:]))/2
pts_count = int(abs(area)) - 0.5*len(visited) +1

print("Solution to Day 10 - part 2:", pts_count)