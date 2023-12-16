from utils import *
from functools import cache

f = open("input.txt", "r")
lines = f.read().split("\n")

# PART 1
energized = set()

#@cache
def create_beam(x, y, dir):
    while x >= 0 and y >= 0 and y < len(lines) and x < len(lines[0])\
            and (x, y, dir) not in energized:
        energized.add((x, y, dir))
        match lines[y][x]:
            case "-":
                if dir[0] == 0:
                    dir = (1, 0)
                    create_beam(x, y, (-1, 0))
            case "|":
                if dir[1] == 0:
                    dir = (0, 1)
                    create_beam(x, y, (0, -1))
            case "/":
                if dir[0] != 0:
                    dir = (0, -dir[0])
                else:
                    dir = (-dir[1], 0)
            case "\\":
                if dir[0] != 0:
                    dir = (0, dir[0])
                else:
                    dir = (dir[1], 0)
            case _:
                pass
        x += dir[0]; y += dir[1]

create_beam(0, 0, (1, 0))

s = set()
for x, y, _ in energized:
    s.add((x, y))

# PART 2
max = 0
for i in range(len(lines)):
    create_beam(0, i, (1, 0))
    s = set()
    for x, y, _ in energized:
        s.add((x, y))
    if (score := len(s)) > max:
        max = score

    energized = set()

for i in range(len(lines)):
    create_beam(len(lines[0])-1, i, (-1, 0))
    s = set()
    for x, y, _ in energized:
        s.add((x, y))
    if (score := len(s)) > max:
        max = score

    energized = set()

for i in range(len(lines[0])):
    create_beam(i, 0, (0, 1))
    s = set()
    for x, y, _ in energized:
        s.add((x, y))
    if (score := len(s)) > max:
        max = score

    energized = set()

for i in range(len(lines[0])):
    create_beam(i, len(lines)-1, (0, -1))
    s = set()
    for x, y, _ in energized:
        s.add((x, y))
    if (score := len(s)) > max:
        max = score

    energized = set()

print(max)

f.close()