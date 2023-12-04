from winning_scratch_cards import process_card

with open("input.txt") as f:
    data = f.read().split("\n")
    data = data[:len(data)-1]

card_dict = {}
card_val = {}
for ind, card in enumerate(data):
    winnings, my_numbers = process_card(card)
    corrects = len([1 for x in my_numbers if x in winnings])
    card_dict[int(ind)] = [int(ind+x) for x in range(1, corrects+1)]

num_of_cards = len(card_dict.keys())

# Count backwards: 
# 1: find the value of the last card
# 2: add the values of all cards, the current card refers to (e.g. card 196 refers to 197, in total 2 cards, 195 refers to 196 and 197, in total 1+2+1 = 4 cards)
# 3: add all values of all cards to find the number of copies of cards
for card_key in list(card_dict.keys())[::-1]:
    value = 0
    referrals = card_dict[card_key]
    if len(referrals) == 0:
        card_val[card_key] = 1
    else:
        card_val[card_key] = 1 + sum([card_val[x] for x in referrals])

print("Answer for Puzzle 8:", sum(list(card_val.values())))