f = open("input.txt", "r")
grid = [list(line.strip("\n")) for line in f.readlines()]

N = len(grid)
M = len(grid[0])

# PART 1 & 2
def weight(grid):
    sum = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "O":
                sum += N-i
    return sum

def roll(xdir, ydir, grid):
    for i in range(N) if ydir <= 0 else range(N-1, -1, -1):
        for j in range(M) if xdir <= 0 else range(M-1, -1, -1):
            if grid[i][j] == "O":
                x, y = j, i
                while x >= -xdir and y >= -ydir and x+xdir < M and y+ydir < N\
                    and grid[y+ydir][x+xdir] == ".":
                    grid[y][x] = "."
                    grid[y+ydir][x+xdir] = "O"
                    y += ydir; x += xdir
    return grid

for _ in range(1_000):
    roll(0, -1, grid)
    roll(-1, 0, grid)
    roll(0, 1, grid)
    roll(1, 0, grid)
# roll(0, -1, grid)
# print("\n".join(["".join(grid[i]) for i in range(N)]))
print(weight(grid))


f.close()