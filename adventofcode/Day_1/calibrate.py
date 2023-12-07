import numpy as np 

input = np.loadtxt("input.txt", dtype=str)

# Find the first and last occurences of numbers
def calibrate_num_line(sentence):
    nums = [x for x in sentence if np.char.isnumeric(x)]
    if len(nums) == 1:
        return str(nums[0]) + str(nums[0])
    return str(nums[0]) + str(nums[-1])

def calibrate(text):
    return sum([int(calibrate_num_line(text[x])) for x in range(len(text))])

if __name__ == "__main__":
    print("Solution to Day 1 - part 1:", calibrate(input))