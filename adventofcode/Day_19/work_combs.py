with open("input.txt") as f:
    workflows = f.read().split("\n\n")[0].split("\n")
    f.close()

workflow_names = [workflows[x][:workflows[x].index("{")] for x in range(len(workflows))]
workflow_rules = [workflows[x].split("{")[1].split("}")[0].split(",") for x in range(len(workflows))]
workflow = dict(zip(workflow_names, workflow_rules))

ranges = [[1, 4000] for _ in range(4)]

token = "in"
combinations = 0

queue = [[ranges, token]]
while len(queue) != 0:
    rang, token = queue.pop(0)
    if token == "A":
        nums = [x[1]-x[0]+1 for x in rang]
        acc = 1
        for num in nums:
            acc *= num 
        combinations += acc
    elif token == "R":
        continue

    else:
        cur = workflow[token]

        for rule in cur:

            if ":" not in rule:
                queue.append([rang, rule])

            else:
                rule, new_token = rule.split(":")

                letter = "xmas".index(rule[0])
                number = int("".join([x for x in rule if x.isdigit()]))

                if "<" in rule:
                    if rang[letter][1] < number:
                        queue.append([rang, new_token])
                        break

                    elif rang[letter][0] > number:
                        pass

                    else:
                        pass_range = [rang[letter][0], number-1]
                        pass_pass = rang.copy()
                        pass_pass[letter] = pass_range
                        queue.append([pass_pass, new_token])

                        deny_range = [number, rang[letter][1]]
                        rang[letter] = deny_range

                elif ">" in rule:
                    if rang[letter][0] > number:
                        queue.append([rang, new_token])
                        break
                    elif rang[letter][1] < number: 
                        pass

                    else:
                        pass_range = [number+1, rang[letter][1]]
                        pass_pass = rang.copy()
                        pass_pass[letter]= pass_range 
                        queue.append([pass_pass, new_token])

                        deny_range = [rang[letter][0], number]
                        rang[letter] = deny_range

print("Solution to Day 19 - Part 2:", combinations)