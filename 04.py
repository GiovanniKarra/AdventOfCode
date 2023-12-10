f = open("input.txt", "r")
lines = f.readlines()

# PART 1
def get_score(winning: list[str], mine: list[str]):
    mineint = [int(elem) for elem in mine]
    winningint = [int(elem) for elem in winning]

    score = 1/2

    for elem in winningint:
        if elem in mineint:
            score *= 2

    return score if score >= 1 else 0

total = 0
for line in lines:
    l = line.split("|")
    l[0] = l[0].split(" ")
    l[0] = [num for num in l[0] if num.isdigit()]
    l[1] = l[1].strip("\n").split(" ")
    l[1] = [num for num in l[1] if num.isdigit()]

    total += get_score(l[0], l[1])

# PART 2
def get_count(winning: list[str], mine: list[str]):
    mineint = [int(elem) for elem in mine]
    winningint = [int(elem) for elem in winning]

    score = 0
    for elem in winningint:
        if elem in mineint:
            score += 1

    return score

N = len(lines)
instances = [1]*N

for i in range(N):
    line = lines[i]
    l = line.split("|")
    l[0] = l[0].split(" ")
    l[0] = [num for num in l[0] if num.isdigit()]
    l[1] = l[1].strip("\n").split(" ")
    l[1] = [num for num in l[1] if num.isdigit()]

    score = get_count(l[0], l[1])
    for j in range(i+1, i+score+1):
        instances[j] += instances[i]

print(sum(instances))

f.close()