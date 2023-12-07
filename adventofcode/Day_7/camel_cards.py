import numpy as np 

card_to_ind = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "T": 10,
               "J": 11,
               "Q": 12,
               "K": 13,
               "A": 14}

with open("input.txt") as f:
    data = [x.split(" ") for x in f.read().split("\n")]
    # data = [  for y in data] ### TO DO: Convert T, J, Q, K, A to ints in the codes for np.bincount


print(data[0])