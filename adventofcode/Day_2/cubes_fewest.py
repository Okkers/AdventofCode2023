from cubes import process_input

with open("input.txt") as f:
    data = f.read()

input_dict = process_input(data)

# Loop through each game and record the maximum number of reds, greens and blues used.
fewest_cubes = {}
fewest_sum = 0
for ind, game in enumerate(input_dict.keys()):
    games = input_dict[game]
    red_cnt = 0
    green_cnt = 0 
    blue_cnt = 0
    for draw in games:
        for sentence in draw: 
            for color in ["red", "green", "blue"]:
                if color in sentence:
                    value = int("".join([x for x in sentence if x.isdigit()]))
                    if color == "red":
                        if value != 0 and value > red_cnt: 
                            red_cnt = value 
                    if color == "green":
                        if value != 0 and value > green_cnt:
                            green_cnt = value 
                    if color == "blue":
                        if value != 0 and value > blue_cnt:
                            blue_cnt = value 
    if red_cnt == 0 or green_cnt == 0 or blue_cnt == 0:
        fewest_cubes[game] = [0]
    else:
        fewest_cubes[game] = [red_cnt*green_cnt*blue_cnt]
        fewest_sum += fewest_cubes[game][0]

print("Solution to Day 2 - part 2:", fewest_sum)