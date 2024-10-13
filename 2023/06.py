f = open("input.txt", "r")
lines = f.readlines()

# PART 1
time = list(filter(lambda x : x != "", lines[0].strip("Time: ").strip("\n").split(" ")))
distance = list(filter(lambda x : x != "", lines[1].strip("Distance: ").strip("\n").split(" ")))

total = 1

for i in range(len(time)):
    t = int(time[i])
    d = int(distance[i])
    wincount = 0

    for ti in range(t):
        speed = ti
        if speed * (t-ti) > d:
            wincount += 1
    
    total *= wincount

# PART 2
time = int("".join([c for c in lines[0] if c.isdigit()]))
distance = int("".join([c for c in lines[1] if c.isdigit()]))


wincount = 0

for t in range(14, time):
    speed = t
    if speed * (time-t) > distance:
        wincount += 1

print(wincount)

f.close()