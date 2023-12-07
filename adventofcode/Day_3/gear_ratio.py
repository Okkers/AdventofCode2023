from gears import within_bounds

with open("input.txt") as f:
    frame = f.read().split("\n")
frame = frame[:len(frame)]

# Given indices, find the whole number recursively, checking the left and right
def find_full_num(arr, ind_x, ind_y):
    visited_sq = []
    def find_full_num_rec(arr, ind_x, ind_y, num, visited):
        if not(within_bounds(ind_x, ind_y, len(arr), len(arr[ind_x]))):
            return num
        if (ind_x, ind_y) in visited:
            return ""
        elif not(arr[ind_x][ind_y].isdigit()):
            return num
        else: 
            visited.append((ind_x, ind_y))
            visited_sq.append((ind_x, ind_y))
            side_1 = find_full_num_rec(arr, ind_x, ind_y - 1, arr[ind_x][ind_y] + num, visited)
            side_2 = find_full_num_rec(arr, ind_x, ind_y + 1, num + arr[ind_x][ind_y], visited)
            return side_1 + side_2

    res = find_full_num_rec(arr, ind_x, ind_y, "", [])
    if ind_y == 0 or ind_y == len(arr[ind_x]):
        return res, visited_sq
    if ind_y+1 == len(arr[ind_x]):
        return res[::-1].replace(arr[ind_x][ind_y], "", 1)[::-1], visited_sq
    elif not(arr[ind_x][ind_y+1].isdigit()):
        return res[::-1].replace(arr[ind_x][ind_y], "", 1)[::-1], visited_sq
    return res.replace(arr[ind_x][ind_y], "", 1), visited_sq

# Loop through the array, if we discover a "*", check the surroundings: if we discover a number, find all indices of the number and record. If 
# two numbers are present, the corresponding gear ratio can be found
adjs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
gear_ratios = []
for s_ind in range(len(frame)):
    for c_ind in range(len(frame[s_ind])):
        if frame[s_ind][c_ind] == "*":
            cnt = 0
            numbers = []
            visited = []
            for ind_x, ind_y in adjs:
                new_x = s_ind + ind_x
                new_y = c_ind + ind_y
                if not(within_bounds(new_x, new_y, len(frame), len(frame[s_ind]))) or (new_x, new_y) in visited:
                    pass
                else:
                    if frame[new_x][new_y].isdigit():
                        number, indices = find_full_num(frame, new_x, new_y)
                        numbers.append(number)
                        for index in indices:
                            visited.append(index)
                        cnt += 1
            if cnt == 2:
                gear_ratios.append(int(numbers[0])*int(numbers[1]))

print("Solution to Day 3 - part 2:", sum(gear_ratios))