from utils import *
from collections import deque

f = open("input.txt", "r")
lines = f.read().split("\n")

N = len(lines); M = len(lines[0])
starting_pos = (0, 0)

for i in range(N):
    for j in range(M):
        if lines[i][j] == "S":
            starting_pos = (j, i)
            break
    if starting_pos != (0, 0): break

# PART 1
def bfs(start, steps):
    count = 1

    visited = set()
    queue = deque()
    d = [[INF]*M for _ in range(N)]

    queue.append(start)
    visited.add(start)
    d[start[1]][start[0]] = 0

    while queue:
        x, y = queue.popleft()
        if d[y][x] > steps: break

        for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dx, dy = x+dir[0], y+dir[1]

            if dx < 0 or dx >= M or dy < 0 or dy >= N or lines[dy][dx] == "#"\
                    or (dx, dy) in visited:
                continue
                
            visited.add((dx, dy))
            queue.append((dx, dy))
            d[dy][dx] = d[y][x]+1

            if d[dy][dx] % 2 == 0: count += 1
            
    return count

# PART 2

f.close()