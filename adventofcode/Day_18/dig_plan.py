from itertools import pairwise

def area(vertices):
    vertices.append(vertices[0])
    inside = abs(
        sum(int(a.real * b.imag - a.imag * b.real) for a, b in pairwise(vertices)) // 2
    )
    boundary = sum(int(abs(a - b)) for a, b in pairwise(vertices)) // 2
    return inside + boundary + 1

dirs = (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j)
pos1 = 0 + 0j
pos2 = 0 + 0j
vertices1 = [pos1]
vertices2 = [pos2]

with open("input.txt", "r") as f:
    for line in f.readlines():
        direction, distance, hex = line.split()
        step = dirs["RDLU".index(direction)]
        pos1 += int(distance) * step
        vertices1.append(pos1)
        distance = int(hex[2:7], 16)
        step = dirs[int(hex[-2])]
        pos2 += int(distance) * step
        vertices2.append(pos2)

print(f"Solution to Day 18 - Part 1: {area(vertices1)}")
print(f"Solution to Day 18 - Part 2: {area(vertices2)}")