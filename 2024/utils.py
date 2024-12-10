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

def product(l):
    p = 1
    for elem in l:
        p *= elem

    return p