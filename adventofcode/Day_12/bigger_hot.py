with open("input.txt") as f:
    data = f.read().split("\n")[:-1]
    springs = []
    for spring_line in data:
        plc1 = spring_line.split(" ")
        ext_spring = "?".join([plc1[0] for _ in range(5)])
        ext_count = ",".join([plc1[1] for _ in range(5)])

        springs.append([ext_spring, ext_count])

configs = 0
for spring, group in springs:
    group = [int(x) for x in group.split(",")]
    states = "."
    for gr in group:
        states += "#"*gr
        states += "."

    states_dict = {0:1}
    new_dict = {}
    for char in spring:
        for state in states_dict:
            if char == "?":
                if state + 1 < len(states):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == ".":
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == "#":
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]

        states_dict = new_dict
        new_dict = {}

    res = states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)
    configs += res 

print("Solution to Day 12 - part 2:", configs)