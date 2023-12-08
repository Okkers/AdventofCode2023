import numpy as np 

card_to_ind = dict(zip("23456789TJQKA", range(2, 15)))

with open("input.txt") as f:
    data = [x.split(" ") for x in f.read().split("\n")]
    cards = []
    for ind in range(len(data)):
        plc = [card_to_ind[x] for x in data[ind][0]]
        cards.append([plc, data[ind][1]])

def find_hand(hand):
    counts = np.bincount(hand[0])
    if 5 in counts:
        return "5"
    if 4 in counts:
        return "4"
    if 3 in counts and 2 in counts:
        return "H"
    if 3 in counts:
        return "3"
    if np.count_nonzero(counts == 2 ) == 2:
        return "TP"
    if 2 in counts:
        return "P"
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
    hands[hand].append(cards[i])

sorted = []
for category in hands.values():
    category.sort(key = lambda x: [x[0][i] for i in range(5)])
    sorted.append(category)
sorted = [x for y in sorted for x in y]

ans = 0
for ind in range(len(sorted)):
    ans += (ind+1)*(int(sorted[ind][1]))
print("Solution to Day 7 - part 1:", ans)