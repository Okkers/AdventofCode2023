with open("input.txt") as f:
    data = f.read().split("\n")
    data = data[:len(data)-1]

def process_card(input):
    plc = input.split(":")[1].split("|")
    winning = [x for x in plc[0].split(" ") if x != ""]
    my_numbers = [x for x in plc[1].split(" ") if x != ""]

    return winning, my_numbers

earnings = 0
for card in data:
    winning, my_numbers = process_card(card)
    value = [2 for x in my_numbers if x in winning]
    if len(value) > 0:
        f, accu = lambda acc, x: acc * x, 1
        earnings += [accu := f(accu, x) for x in value][-1]//2

if __name__ == "__main__":
    print("Answer for Puzzle 7:", earnings)