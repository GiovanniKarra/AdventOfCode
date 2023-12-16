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