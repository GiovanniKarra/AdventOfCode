def getID(s):
    n = s.split(":")
    id = int(n[0][5:])
    return id


def getRGB(s):
    r, g, b = 0, 0, 0
    n = s.replace("\n", "").replace(",", "").split(" ")
    if "red" in n:
        r = int(n[n.index("red")-1])
    if "green" in n:
        g = int(n[n.index("green")-1])
    if "blue" in n:
        b = int(n[n.index("blue")-1])
    return r, g, b


f = open("input.txt", "r")
lines = f.readlines()

# PART 1
validIDs = []

rMax = 12
gMax = 13
bMax = 14

for line in lines:
    id = getID(line)
    rolls = line.split(";")
    valid = True
    for roll in rolls:
        r, g, b = getRGB(roll)
        if r > rMax or g > gMax or b > bMax:
            valid = False
            break
    if valid:
        validIDs.append(id)

# PART 2
powers = []

for line in lines:
    id = getID(line)
    rolls = line.split(";")
    valid = True
    rMin, gMin, bMin = 0, 0, 0
    for roll in rolls:
        r, g, b = getRGB(roll)
        if r > rMin:
            rMin = r
        if g > gMin:
            gMin = g
        if b > bMin:
            bMin = b

    powers.append(rMin*gMin*bMin)

print(sum(powers))

f.close()