f = open("input.txt", "r")
lines = [list(line.strip("\n")) for line in f.readlines()]

N = len(lines)
M = len(lines[0])

# PART 1
def get_empty():
    l = []; col = []

    for i in range(N):
        if all(char == "." for char in lines[i]):
            l.append(i)
    for i in range(M):
        if all(lines[j][i] == "." for j in range(N)):
            col.append(i)

    return tuple(l), tuple(col)

def expand():
    l, col = get_empty()
    for i in range(len(l)):
        lines.insert(l[i]+i, ["." for _ in range(M)])
    dN = len(l)
    dM = len(col)
    for i in range(len(col)):
        for j in range(N+dN):
            lines[j].insert(col[i]+i, ".")

    return dN, dM

def get_num():
    points = dict()
    counter = 1
    for i in range(N):
        for j in range(M):
            if lines[i][j] == "#":
                points[counter] = (j, i)
                counter += 1
    return points, counter-1

def get_pairs(max):
    pairs = set()
    for i in range(1, max):
        for j in range(i+1, max+1):
            pairs.add((i, j))

    return pairs

def manhattan_dist(a: (int, int), b: (int, int)):
    return abs(b[1]-a[1]) + abs(b[0]-a[0])

# dN, dM = expand()
# N += dN; M += dM
# points, max = get_num()
# pairs = get_pairs(max)

# sum = 0
# for pair in pairs:
#     a, b = pair
#     sum += manhattan_dist(points[a], points[b])

# PART 2
def get_num2(l, col):
    points = dict()
    counter = 1
    for i in range(N):
        for j in range(M):
            if lines[i][j] == "#":
                points[counter] =\
                    (j+len(list(filter(lambda x: x < j, col)))*999999,
                     i+len(list(filter(lambda x: x < i, l)))*999999)
                counter += 1
    return points, counter-1

l, col = get_empty()
points, max = get_num2(l, col)
pairs = get_pairs(max)

sum = 0
for pair in pairs:
    a, b = pair
    sum += manhattan_dist(points[a], points[b])

print(sum)

f.close()