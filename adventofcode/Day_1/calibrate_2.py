import numpy as np 
from calibrate import calibrate_num_line

input = np.loadtxt("input.txt", dtype=str)

char_to_num_dict = {"one": 1,
                    "two": 2,
                    "three": 3,
                    "four": 4,
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9}

# Convert words to numbers, without double-counting chars, e.g. "eightwo"
def convert_char_to_num(sentence):
    for num in char_to_num_dict.keys():
        if num in sentence:
            sentence = sentence.replace(num, num+str(char_to_num_dict[num])+num)
    return sentence

def convert_all(text):
    return [convert_char_to_num(text[x]) for x in range(len(text))]

new_sentence = convert_all(input)
print("Solution to Day 1 - part 2:", sum([int(calibrate_num_line(new_sentence[x])) for x in range(len(new_sentence))]))