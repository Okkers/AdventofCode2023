# Load data
with open("input.txt") as f:
    frame = f.read().split("\n")
frame = frame[:len(frame)-1]

# Check bounds in the array
def within_bounds(x,y, shape1, shape2):
    if x != -1 and x != shape1 and y != -1 and y != shape2:
        return True
    return False

nums_to_add = []
adjs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
s_ind = 0
c_ind = 0

# Loop through the array - if we discover a number, find the adjacent values: if a value isn't a number nor ".", it must 
# be a symbol, and the number is valid
while s_ind != len(frame):
    while c_ind != len(frame[s_ind]):
        if frame[s_ind][c_ind].isdigit():
            check = False
            num = ""
            while frame[s_ind][c_ind].isdigit():
                num += frame[s_ind][c_ind]
                for ind_x, ind_y in adjs:
                    new_x = s_ind + ind_x 
                    new_y = c_ind + ind_y
                    if within_bounds(new_x, new_y, len(frame), len(frame[s_ind])):
                        if frame[new_x][new_y] != "." and not(frame[new_x][new_y].isdigit()):
                            check = True 
                c_ind += 1 
                if c_ind == len(frame[0]):
                    break
            if check:
                nums_to_add.append(num)
        else:
            c_ind += 1
    c_ind = 0
    s_ind += 1

if __name__ == "__main__":
    print("Solution to Day 3 - part 1:", sum([int(x) for x in nums_to_add]))