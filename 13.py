from utils import *

f = open("input.txt", "r")
patterns = [pat.strip("\n").split("\n") for pat in f.read().split("\n\n")]

# PART 1
# @printret
def find_patterns(pat, coef, old = (0, 0)):
    sum = 0
    mirrors = set()
    m = []
    for i in range(len(pat)-1):
        for j in range(i+1, len(pat)):
            if pat[i] == pat[j]:
                mirrors.add((i, j))
    refs = [(i, j) for i, j in mirrors if j == i+1]
    for ref in refs:
        i, j = ref
        while i >= 0 and j < len(pat):
            if (i, j) not in mirrors:
                ref = None
                break
            i -= 1; j += 1
        if ref is not None:
            m.append(ref)
    m = [elem for elem in m if elem != old]
    if len(m) == 0: m = [(0, 0)]
    sum = m[0][1]*coef
    return sum, m

def transpose(pattern):
    toret = []
    for i in range(len(pattern[0])):
        text = ""
        for j in range(len(pattern)):
            text += pattern[j][i]
        toret.append(text)

    return toret

sum = 0
for pat in patterns:
    sum += find_patterns(pat, 100)[0]+find_patterns(transpose(pat), 1)[0]

# PART 2
def distance(a, b):
    diff = 0
    indices = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            indices.append(i)
    return diff, indices

def correction(pat):
    toret = pat
    change = False
    tocheck = []
    for i in range(len(pat)-1):
        for j in range(i+1, len(pat)):
            if distance(pat[i], pat[j])[0] == 1:
                tocheck.append((i, distance(pat[i], pat[j])[1][0], j))
    _, ref = find_patterns(pat, 0)
    if len(ref) == 0:
        ref = (0, 0)
    else:
        ref = ref[0]
    for i, j, k in tocheck:
        newpat = [list(elem) for elem in pat]
        newpat2 = [list(elem) for elem in pat]
        if newpat[i][j] == "#":
            newpat[i][j] = "."
        else:
            newpat[i][j] = "#"
        if newpat2[k][j] == "#":
            newpat2[k][j] = "."
        else:
            newpat2[k][j] = "#"
        newpat = ["".join(elem) for elem in newpat]
        newpat2 = ["".join(elem) for elem in newpat2]
        if any(r != ref for r in find_patterns(newpat, 0)[1]):
            toret = newpat
            change = True
            break
        if any(r != ref for r in find_patterns(newpat2, 0)[1]):
            toret = newpat2
            change = True
            break
    return toret, change


sum = 0
for pat in patterns:
    olds = (find_patterns(pat, 100)[1][0], find_patterns(transpose(pat), 1)[1][0])

    ch2 = False
    pat2, ch = correction(pat)
    trans = transpose(pat2)
    if not ch:
        trans, ch2 = correction(transpose(pat))
        pat2 = transpose(trans)
        print("\n".join(pat))
        print()
        print("\n".join(pat2))
    sum += find_patterns(pat2, 100, olds[0])[0]*int(ch)+find_patterns(trans, 1, olds[1])[0]*int(ch2)
    #print()

print(sum)

f.close()