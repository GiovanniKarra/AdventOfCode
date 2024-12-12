INF = float("inf")

def printret(func):
    def wrapper(*args):
        val = func(*args)
        print(val)
        return val

    return wrapper

def printretarg(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print(f"args : {args}, " + f"kwargs : {kwargs}, "*int(len(kwargs) > 0) + f"ret : {val}")
        return val

    return wrapper

def grid_to_string(grid):
    return "\n".join(["".join(line) for line in grid])

def to_grid(string):
    grid = [list(line) for line in string.split("\n")]
    m, n = len(grid), len(grid[0])
    return grid, m, n

def product(l):
    p = 1
    for elem in l:
        p *= elem

    return p