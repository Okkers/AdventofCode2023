with open("input.txt") as f:
    data = f.read().split(":")
    plc= data[1].split("\n")
    times = [ x for x in plc[:len(plc)-1][0].split(" ") if x != ""]
    d_plc = data[2].split("\n")
    dists = [x for x in d_plc[:len(d_plc)-1][0].split(" ") if x != ""]

winnings = []
for indx in range(len(dists)):
    num_win = 0
    secs = int(times[indx])
    dist = int(dists[indx])
    for hold_button_down in range(secs):
        dist_reached = hold_button_down * (secs-hold_button_down)
        if dist_reached > dist:
            num_win += 1
    winnings.append(num_win)

f = lambda acc, x: acc *x 
accu = 1
[accu := f(accu, x) for x in winnings]

print("Solution to Day 6 - part 1:", accu)