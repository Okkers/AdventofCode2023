import math

walks = {}
start_points = []

with open("input.txt") as f:
    data = f.read().split("\n\n")
    directions = data[0]
    nodes = data[1].split("\n")
    for i in range(len(nodes)-1):
        if nodes[i][2] == "A":
            start_points.append(nodes[i][:3])
        walks[nodes[i][:3]] = [nodes[i][7:10], nodes[i][12:15]]

cnts = []
while len(start_points) != 0:
    start = start_points.pop()
    cnt = 0
    dir = 0
    while start[2] != "Z":
        if directions[dir] == "L":
            start = walks[start][0]
        if directions[dir] == "R":
            start = walks[start][1]
        if dir == len(directions)-1:
            dir = 0 
        else:
             dir += 1
        cnt += 1
    cnts.append(cnt)

ans = 1
[ans := math.lcm(ans,x) for x in cnts]

print("Solution to Day 8 - part 1:", ans)