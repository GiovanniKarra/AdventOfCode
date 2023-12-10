f = open("input.txt", "r")
lines = f.readlines()
lines = [list(line.strip()) for line in lines]

# PART 1
pipes = {"|": {0, 2}, "-": {1, 3}, "L": {0, 1}, ".": {},
         "J": {0, 3}, "F": {1, 2}, "7": {2, 3}, "S": {0, 1, 2, 3}}

def find_next(x, y, type, prev):
    directions = pipes[type].difference({prev})

    if 0 in directions:
        if 2 in pipes[lines[y-1][x]]:
            return x, y-1, 2
    if 1 in directions:
        if 3 in pipes[lines[y][x+1]]:
            return x+1, y, 3
    if 2 in directions:
        if 0 in pipes[lines[y+1][x]]:
            return x, y+1, 0
    if 3 in directions:
        if 1 in pipes[lines[y][x-1]]:
            return x-1, y, 1

x_init, y_init = 0, 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "S":
            x_init, y_init = j, i

x, y, prev = find_next(x_init, y_init, "S", 4)
length = 1
path = [(x, y)]
while (x, y) != (x_init, y_init):
    x, y, prev = find_next(x, y, lines[y][x], prev)
    length += 1
    path.append((x, y))

length //= 2

# PART 2
N = len(path)
Area = abs(0.5*sum([(path[i][1]+path[(i+1)%N][1])*(path[i][0]-path[(i+1)%N][0])
                for i in range(N)]))
num = Area + 1 - length

print(num)

f.close()