with open("input.txt") as f:
    data = f.read().split("\n")[:-1]
    data = [[int(z) for z in x.split(" ")] for x in data]

def get_diffs(lst):
    diff_dict = {}
    diffs = []
    end = False
    cnt = 0
    while not end:
        for i in range(len(lst)-1):
            diffs.append(lst[i+1]-lst[i])
        if diffs.count(0) == len(diffs):
            diffs.append(0)
            diff_dict[cnt] = diffs
            end = True 
        else:
            diff_dict[cnt] = diffs
            lst = diffs 
            diffs = []
            cnt += 1

    return diff_dict

last_vals = []
for ind,oasis in enumerate(data):
    diff_dict = get_diffs(oasis)
    for ind,key in enumerate(list(diff_dict.keys())[::-1]):
        if key == 0:
            last_vals.append(oasis[-1]+diff_dict[key][-1])
        else:
            diff_dict[key-1].append(diff_dict[key-1][-1] + diff_dict[key][-1])

print("Solution to Day 9 - part 1:", sum(last_vals))