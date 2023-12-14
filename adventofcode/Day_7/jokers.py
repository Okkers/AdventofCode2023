import numpy as np 
from collections import Counter

card_to_ind = dict(zip("23456789TJQKA", range(2, 15)))

with open("input.txt") as f:
    data = [x.split(" ") for x in f.read().split("\n")]
    cards = []
    for ind in range(len(data)):
        plc = [card_to_ind[x] for x in data[ind][0]]
        cards.append([plc, data[ind][1]])

def find_hand(hand):
    jokers = hand[0].count(11)
    counts = np.bincount(hand[0])
    if len(counts) > 11:
        counts[11] = 0
    if 5 in counts:
        return "5"
    if 4 in counts:
        if jokers == 1:
            return "5"
        return "4"
    if 3 in counts and 2 in counts:
        if jokers == 1:
            return "4"
        if jokers == 2:
            return "5"
        return "H"
    if 3 in counts:
        if jokers == 1:
            return "4"
        if jokers == 2:
            return "5"
        return "3"
    if np.count_nonzero(counts == 2 ) == 2:
        if jokers == 1:
            return "H"
        if jokers == 2:
            return "4"
        if jokers == 3:
            return "5"
        return "TP"
    if 2 in counts:
        if jokers == 1:
            return "3"
        if jokers == 2:
            return "4"
        if jokers == 3:
            return "5"
        return "P"
    if jokers == 1:
        return "P"
    if jokers == 2:
        return "3"
    if jokers == 3:
        return "4"
    if jokers == 4:
        return "5"
    if jokers == 5:
        return "5"
    return "HC"

hands = {"HC": [],
         "P": [],
         "TP": [],
         "3": [],
         "H": [],
         "4": [],
         "5": []}

for i in range(len(cards)):
    hand = find_hand(cards[i])
    hands[hand].append([[x if x != 11 else 0 for x in cards[i][0]], cards[i][1]])

sorted = []
for category in hands.values():
    category.sort(key = lambda x: [x[0][i] for i in range(5)])
    sorted.append(category)
sorted = [x for y in sorted for x in y]

ans = 0
for ind in range(len(sorted)):
    ans += (ind+1)*(int(sorted[ind][1]))
print("Solution to Day 7 - part 1:", ans)