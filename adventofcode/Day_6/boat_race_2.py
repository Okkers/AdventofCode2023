with open("input.txt") as f:
    data = f.read().split(":")
    plc= data[1].split("\n")
    time = int("".join([ x for x in plc[:len(plc)-1][0].split(" ") if x != ""]))
    d_plc = data[2].split("\n")
    dist = int("".join([x for x in d_plc[:len(d_plc)-1][0].split(" ") if x != ""]))

ind = 0 
found = False 
ans = 0
while not(found):
    dist_reached = ind*(time-ind)
    if dist_reached > dist:
        ans = time-ind-ind+1 
        print(ind)
        found = True 
    else:
        ind += 1

print("Solution to Day 6 - part 2:", ans)