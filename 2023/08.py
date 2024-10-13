from math import lcm

f = open("input.txt", "r")
lines = f.readlines()

# PART 1
instructions = lines[0].strip("\n")
N = len(instructions)
nodes = dict()

for i in range(2, len(lines)):
    line = lines[i]
    tmp = line.split("=")
    node = tmp[0].strip()
    dir = tuple(tmp[1].strip().strip("\n")[1:-1].split(", "))
    nodes[node] = dir

def stepcount(a, b):
    current_node = a
    steps = 0

    while current_node != b:
        direction = 0 if instructions[steps%N] == "L" else 1
        current_node = nodes[current_node][direction]
        steps += 1

    return steps


# PART 2
def find_ending_A():
    toret = []
    for elem in nodes.keys():
        if elem[2] == "A":
            toret.append(elem)
    return toret

def ending_Z(nodes):
    for elem in nodes:
        if elem[2] != "Z":
            return False
    return True

current_nodes = find_ending_A()
indices = []
steps = 0

for i in range(len(current_nodes)):
    steps = 0

    while current_nodes[i][2] != "Z":
        direction = 0 if instructions[steps%N] == "L" else 1
        current_nodes[i] = nodes[current_nodes[i]][direction]
        steps += 1
    indices.append(steps)

final = lcm(*indices)
print(final)

f.close()