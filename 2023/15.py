from utils import *

f = open("input.txt", "r")
codes = [line.strip("\n") for line in f.read().split(",")]

# PART 1
def hash(s: str):
    code = 0
    for char in s:
        code += ord(char)
        code *= 17
        code %= 256
    return code

sum = 0
for code in codes:
    sum += hash(code)

# PART 2
def contains_label(box: list[tuple[str, int]], label: str):
    for i in range(len(box)):
        l = box[i][0]
        if label == l:
            return i
    return -1

table = [[] for _ in range(256)]

for code in codes:
    if "=" in code:
        label, lens = code.split("=")
        lens = int(lens)
        box = table[hash(label)]
        if (index := contains_label(box, label)) != -1:
            box[index] = (label, lens)
        else:
            box.append((label, lens))
    elif "-" in code:
        label = code[:-1]
        box = table[hash(label)]
        if (index := contains_label(box, label)) != -1:
            box.remove(box[index])

sum = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        sum += (i+1)*(j+1)*table[i][j][1]

print(sum)

f.close()