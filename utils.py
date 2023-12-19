def printret(func):
    def wrapper(*args):
        val = func(*args)
        print(val)
        return val

    return wrapper

def printretarg(func):
    def wrapper(*args):
        val = func(*args)
        print(f"args : {args}, ret : {val}")
        return val

    return wrapper

def grid_to_string(grid):
    return "\n".join(["".join(line) for line in grid])

def product(l):
    p = 1
    for elem in l:
        p *= elem

    return p