from utils import *

f = open("input.txt", "r")
lines = f.read().split("\n")

lines = [line.split(" ") for line in lines]
lines = [(direction, int(dist), color.strip("()")) for direction, dist, color in lines]

directions = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

# PART 1
x, y = 0, 0
outline = []
for dir, dist, _ in lines:
    dir = directions[dir]
    for _ in range(dist):
        x += dir[0]; y += dir[1]
        outline.append((x, y))

boundry_points = len(outline)
area = 0
for i in range(boundry_points):
    area += (outline[i][1]+outline[(i+1)%boundry_points][1])*\
                (outline[i][0]-outline[(i+1)%boundry_points][0])
area *= 0.5
interior_points = area + 1 - 0.5*boundry_points

count = boundry_points + interior_points

# PART 2
for i in range(len(lines)):
    _, _, color = lines[i]
    new_dir = "R" if color[-1] == "0" else "D" if color[-1] == "1"\
        else "L" if color[-1] == "2" else "U"
    new_dist = int(color[1:-1], 16)
    lines[i] = (new_dir, new_dist)

# x, y = 0, 0
# outline = []
# boundry_points = 0
# area = 0
# for dir, dist in lines:
#     dir = directions[dir]
#     boundry_points += dist

#     x += dir[0]*dist; y += dir[1]*dist

#     if dir[0] == 0: continue
#     area += 2*y*dist

# area *= 0.5
# interior_points = area + 1 - 0.5*boundry_points

x, y = 0, 0
outline = []
boundry_points = 0
for dir, dist in lines:
    dir = directions[dir]
    boundry_points += dist
    x += dir[0]*dist; y += dir[1]*dist
    outline.append((x, y))

area = 0
for i in range(len(outline)):
    area += (outline[i][1]+outline[(i+1)%len(outline)][1])*\
                (outline[i][0]-outline[(i+1)%len(outline)][0])
area *= 0.5
interior_points = area + 1 - 0.5*boundry_points

count = boundry_points + interior_points
print(count)

f.close()