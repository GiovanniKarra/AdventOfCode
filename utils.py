def printret(func):
    def wrapper(*args):
        val = func(*args)
        print(val)
        return val

    return wrapper
