import numpy as np

garden = np.genfromtxt("input.txt", comments=None, delimiter=1, dtype=str).astype(str)
start = tuple([x[0] for x in np.where(garden == "S")])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

max_1 = 64
max_2 = 26501365

def parse_input():
    with open("input.txt") as f:
        lines = tuple(l.strip() for l in f.readlines())
    return lines

def bfs(grid, steps, start):
    v = {start: 0}
    dist = 0
    q = []
    q.append(start)
    result = []
    while dist < max(steps):
        dist += 1
        new_q = []
        while len(q) != 0:
            x, y = q.pop(0)   
            for ind_x, ind_y in dirs:
                new_x, new_y = x + ind_x, y + ind_y
                fit_x, fit_y = new_x % len(grid[0]), new_y % len(grid)
                if grid[fit_x,fit_y] != '#' and (new_x, new_y) not in v:
                    v[(new_x, new_y)] = dist
                    new_q.append((new_x, new_y))
        q = new_q
        if dist in steps:
            result.append(len([x for x in v.values() if x % 2 == dist % 2]))
    return result

ans1 = bfs(garden, [max_1], start)[0]
print("Solution to Day 21 - part 1:", ans1)

s, h = len(garden), start[0]
diamond_sizes = [h, s+h, 2*s+h]
funcs = bfs(garden, diamond_sizes, start)
# Polynomial
a = (funcs[2] - 2*funcs[1] + funcs[0]) // 2
b = funcs[1] - funcs[0] - a 
poly = lambda x: a*x**2 + b*x + funcs[0]
n = (max_2 - h)//s

print("Solution to Day 21 - part 2:", poly((max_2 - h)//s))


