with open("input.txt") as f:
    data = f.read().split("\n\n")
    f.close()

workflows = data[0].split("\n")
items = data[1].split("\n")

workflow_names = [workflows[x][:workflows[x].index("{")] for x in range(len(workflows))]
workflow_rules = [workflows[x].split("{")[1].split("}")[0].split(",") for x in range(len(workflows))]

workflow = dict(zip(workflow_names, workflow_rules))

rating_numbers = 0

for item in items:
    x, m, a, s = [int("".join([x for x in y if x.isdigit()])) for y in item.split(",")]
    token = "in"
    sorted = False

    while not sorted: 
        if token == "A":
            rating_numbers += x+m+a+s
            sorted = True 

        elif token == "R":
            sorted = True 

        else:
            cur = workflow[token]  
            for rule in cur:
                if ":" not in rule:
                    token = rule
                    break

                else:
                    rule = rule.split(":")
                    if eval(rule[0]):
                        token = rule[1]
                        break

print("Solution to Day 19 - Part 1:", rating_numbers)