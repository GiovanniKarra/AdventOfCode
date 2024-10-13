from collections import deque
from math import lcm
from utils import *

f = open("input.txt", "r")
lines = f.read().split("\n")

nodes = dict()
BROAD, FLIPFLOP, JUNC = 10, 11, 12
LOW, HIGH = 0, 1

for line in lines:
    name, dest = line.split(" -> ")

    node_type = BROAD
    state = None
    if name[0] == "%":
        name = name[1:]
        node_type = FLIPFLOP
        state = False
    elif name[0] == "&":
        name = name[1:]
        node_type = JUNC
        state = dict()

    dest = tuple(dest.strip().split(", "))

    nodes[name] = [node_type, state, dest]

for node in nodes.keys():
    info = nodes[node]
    for dest in info[2]:
        try:
            if nodes[dest][0] == JUNC:
                nodes[dest][1][node] = LOW
        except KeyError:
            continue

# PART 1
queue = deque()
count = [0, 0]
reset_counter = 0

for _ in range(1000):
# out = False
# dif = [0]
# while not out:
    queue.append(("broadcaster", LOW, "input"))
    reset_counter += 1
    while queue:
        name, pulse, origin = queue.popleft()
        if name == "rx" and pulse == LOW:
            out = True
            break
        count[pulse] += 1
        try:
            node = nodes[name]
        except KeyError:
            continue

        if node[0] == BROAD:
            for dest in node[2]:
                queue.append((dest, LOW, name))
        elif node[0] == FLIPFLOP:
            if pulse == HIGH: continue
            stat = node[1]
            node[1] = not stat
            tosend = LOW if stat else HIGH
            for dest in node[2]:
                queue.append((dest, tosend, name))
        else:
            node[1][origin] = pulse
            tosend = HIGH
            if all(p == HIGH for p in node[1].values()): tosend = LOW
            for dest in node[2]:
                queue.append((dest, tosend, name))
        # nb : 3851 vg : 3931 vc : 3881 ls : 3943
        if nodes["lg"][1]["ls"] == HIGH:
            print(reset_counter)

print(count[0]*count[1])
print(lcm(3851, 3931, 3881, 3943))

f.close()