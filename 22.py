f = open("input.txt", "r")
lines = f.read().split("\n")
bricks = [tuple(tuple(int(x) for x in coord.split(","))
                for coord in line.split("~")) for line in lines]



f.close()