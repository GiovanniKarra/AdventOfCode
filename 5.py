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
    seeds.append(range(pair[0], pair[0]+pair[1]))

def intersect(a: range, b: range):
    return a.start < b.stop and a.stop > b.start


def divide(a: list[range], b: range):
    toret = []
    for r in a:
        if r.start <= b.start:
            toret.append(range(r.start, b.start))
            if r.stop >= b.stop:
                toret.append(range(b.stop, r.stop))
        elif r.start < b.stop:
            if r.stop >= b.stop:
                toret.append(range(b.stop, r.stop))
        else:
            toret.append(r)

    return toret


def find_ran(rans: list[range], mapnum: int):
    toret = []
    map = maps[mapnum]
    no_intersect = rans.copy()
    for ran in rans:
        for m in map:
            if intersect(ran, range(m[1], m[1]+m[2])):
                diffstart = max(ran.start - m[1], 0)
                diffstop = min(ran.stop - m[1], m[2])
                toret.append(range(m[0] + diffstart, m[0] + diffstop))
        
    for m in map:
        mr = range(m[1], m[1]+m[2])
        no_intersect = divide(no_intersect, mr)

    for e in no_intersect: toret.append(e)

    return toret

minloc = 999999999999999999999999999999999
for ran in seeds:
    val = [ran]
    for i in range(7):
        val = find_ran(val, i)
    if (m := min(v.start for v in val)) < minloc:
        minloc = m

print(minloc)

f.close()