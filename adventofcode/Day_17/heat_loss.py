import numpy as np
from queue import PriorityQueue

heat_path = np.genfromtxt("input.txt", comments=None, delimiter=1).astype(int)
#NOT DONE

def within_bounds(arr, ind):
    if ind[0] >= 0 and ind[0] < arr.shape[0] and ind[1] >= 0 and ind[1] < arr.shape[1]:
        return True
    return False

def navigate(grid, minval=1, maxval=3):
    q = PriorityQueue()
    max_y, max_x = (v - 1 for v in grid.shape)
    goal = max_y, max_x
    q.put((0, (0, 0, 0)))
    q.put((0, (0, 0, 1)))
    seen = set()

    while q:
        cost, (y, x, direction) = q.get()
        if (y, x) == goal:
            break
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        original_cost = cost
        for s in [-1, 1]:
            cost = original_cost
            new_y, new_x = y, x
            for i in range(1, maxval + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                cost += grid[new_y, new_x]
                if ((new_y, new_x, 1 - direction)) in seen:
                    continue
                if i >= minval:
                    q.put((cost, (new_y, new_x, 1 - direction)))
    return cost

ans1 = navigate(heat_path, 1, 3)
ans2 = navigate(heat_path, 4, 10)
print("Solution to Day 17 - part 1:", ans1)
print("Solution to Day 17 - part 2:", ans2)