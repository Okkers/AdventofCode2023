bag_amounts = { "red": 12,
               "green": 13,
               "blue": 14
}

with open("input.txt") as f:
    data = f.read()

def process_input(data):
    data = data.split("\n")

    input_dict = {}
    for sentence in data:
        plc = sentence.split(":")
        cube_draws = plc[1].split(";")
        build = []
        for draw in cube_draws: 
            games = draw.split(",")
            build.append(games)
        input_dict[plc[0]] = build

    return input_dict
input_dict = process_input(data)

correct_dict = {}
correct_games = []

for ind, game in enumerate(input_dict.keys()):
    games = input_dict[game]
    # [[]]
    for draw in games:
        #[], [], []#
        for sentence in draw: 
            for color in bag_amounts.keys():
                if color in sentence:
                    check = int("".join([x for x in sentence if x.isdigit()]))
                    if check > bag_amounts[color]:
                        correct_dict[game] = False
        if game not in correct_dict.keys():
            correct_dict[game] = True
    if correct_dict[game]:
        correct_games.append(ind+1)  

if __name__ == "__main__":
    print("Answer for Puzzle 3:", sum(correct_games))