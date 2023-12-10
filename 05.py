from utils import *

f = open("input.txt")
lines = f.readlines()

# PART 1
seeds = lines[0].strip("seeds: ").strip("\n").split(" ")
seeds = [int(seed) for seed in seeds]
maps = [[] for _ in range(7)]


def find_num(val: int, mapnum: int):
    map = maps[mapnum]
    for m in map:
        if val >= m[1] and val < m[1] + m[2]:
            diff = val - m[1]
            return m[0] + diff
        
    return val

i = 3
map_num = 0
while i < len(lines):
    line = lines[i]
    if line == "\n":
        i += 1
        map_num += 1
    else:
        map = line.strip("\n").split(" ")
        map = tuple(int(num) for num in map)
        maps[map_num].append(map)
    i += 1

minloc = 999999999999999999999999999999999999999999999
for seed in seeds:
    val = seed
    for i in range(7):
        val = find_num(val, i)
    if val < minloc:
        minloc = val

# PART 2
seedranges = lines[0].strip("seeds: ").strip("\n").split(" ")
seedranges = [(int(seedranges[i]), int(seedranges[i+1])) for i in range(0, len(seedranges), 2)]
seeds = []

for pair in seedranges:
    seeds.append((pair[0], pair[0]+pair[1]-1))

def intersect(a: (int, int), b: (int, int)):
    return a[0] <= b[1] and a[1] >= b[0]

def union(a: list[(int, int)]):
    b = []
    for begin,end in sorted(a):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return [tuple(e) for e in b]


def divide(a: list[(int, int)], b: (int, int)):
    toret = []
    for r in a:
        if r[0] < b[0]:
            toret.append((r[0], b[0]-1))
            if r[1] > b[1]:
                toret.append((b[1]+1, r[1]))
        elif r[0] < b[1]:
            if r[1] > b[1]:
                toret.append((b[1]+1, r[1]))
        else:
            toret.append(r)

    return union(toret)


def find_ran(rans: list[(int, int)], mapnum: int):
    toret = []
    map = maps[mapnum]
    for ran in rans:
        for m in map:
            if intersect(ran, (m[1], m[1]+m[2]-1)):
                diffstart = max(ran[0] - m[1], 0)
                diffstop = min(ran[1] - m[1], m[2]-1)
                toret.append((m[0] + diffstart, m[0] + diffstop))

    return union(toret)

minloc = 999999999999999999999999999999999
for ran in seeds:
    val = [ran]
    for i in range(7):
        val = find_ran(val, i)
    if (m := min([v[0] for v in val]+[9999999999999999999])) < minloc:
        minloc = m

print(minloc)

f.close()