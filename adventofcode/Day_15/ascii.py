with open("input.txt") as f:
    data = f.read().split("\n")[0].split(",")
    f.close()

def HASH(string):
    cur = 0
    for char in string:
        ascii = ord(char)
        cur += ascii
        cur *= 17
        cur = cur % 256
    return cur
vals = [HASH(x) for x in data]

print("Solution to Day 15 - part 1:", sum(vals))

boxes = {}
for string in data:
    if "=" in string:
        plc = string.split("=")
        label, focal, operation = plc[0], plc[1], "="
    elif "-" in string:
        label = string.split("-")[0]
        operation = "-"
    
    box = HASH(label)

    if "-" in string:
        if box in boxes.keys():
            boxes[box] = [x for x in boxes[box] if label not in x]
        
    elif "=" in string:
        new_lens = label + " " + focal
        if box not in boxes.keys():
            boxes[box] = [new_lens]
        else:
            in_box = False
            for ind, lens in enumerate(boxes[box]):
                if label in lens:
                    boxes[box][ind] = new_lens
                    in_box = True
            if not in_box:
                boxes[box].append(new_lens)

focus_power = 0
for box in boxes:
    for ind,lens in enumerate(boxes[box]):
        focus_power += (box+1) * (ind+1) * int(lens[-1])

print("Solution to Day 15 - part 2:", focus_power)

