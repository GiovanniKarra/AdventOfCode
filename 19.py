from utils import *

f = open("input.txt", "r")
rulelines, items = f.read().split("\n\n")
rulelines = rulelines.split("\n")

rules = dict()

for line in rulelines:
    name, rule = line.split("{")
    rule = rule.strip("}").split(",")
    rule = [tuple(elem.split(":")) for elem in rule]

    rules[name] = rule

items = ["".join(filter(lambda x: x.isdigit() or x == ",", item)).split(",")
         for item in items.split("\n")]
items = [tuple(int(val) for val in item) for item in items]

# PART 1
def evaluate(item: tuple[int]):
    rule_name = "in"
    x, m, a, s = item

    while True:
        rule = rules[rule_name]
        for r in rule:
            if len(r) == 1:
                goto = r[0]
                if goto == "A": return True
                elif goto == "R": return False
                else:
                    rule_name = goto
                    break

            test, goto = r
            if eval(test):
                if goto == "A": return True
                elif goto == "R": return False
                else:
                    rule_name = goto
                    break

res = 0
for item in items:
    if evaluate(item):
        res += sum(item)

# PART 2
def dist(t):
    return t[1]-t[0]+1

def check(letter, interval, test):
    a, b = interval
    if letter in test:
        num = int(test[2:])
        if "<" in test:
            if a < num:
                if b < num:
                    return interval, ()
                else:
                    return (a, num-1), (num, b)
            else:
                return False
        else:
            if b > num:
                if a > num:
                    return interval, ()
                else:
                    return (num+1, b), (a, num)
            else:
                return False
    else: return False

def get_prod(t, go, letter):
    p = 1
    text = "xmas"
    for i in range(len(t)):
        if letter == text[i]:
            p *= dist(go)
        else:
            p *= dist(t[i])
    return p

def calc(rule, index, xnum, mnum, anum, snum):
    r = rule[index]
    if len(r) == 1:
        if r[0] == "R": return 0
        elif r[0] == "A": return dist(xnum)*dist(mnum)*dist(anum)*dist(snum)
        else: return calc(rules[r[0]], 0, xnum, mnum, anum, snum)

    test, goto = r
    letters = "xmas"

    for char in letters:
        inter = xnum if char == "x" else mnum if char == "m" else anum if char == "a"\
                                        else snum
        if (intervals := check(char, inter, test)):
            go, cont = intervals
            if cont == ():
                if goto == "R": return 0
                elif goto == "A": return dist(xnum)*dist(mnum)*dist(anum)*dist(snum)
                else: return calc(rules[goto], 0, xnum, mnum, anum, snum)
            else:
                # print(go, char, test, goto)
                tmp = 0 if goto == "R"\
                    else get_prod((xnum, mnum, anum, snum), go, char) if goto == "A"\
                    else calc(rules[goto], 0, go, mnum, anum, snum) if char == "x"\
                    else calc(rules[goto], 0, xnum, go, anum, snum) if char == "m"\
                    else calc(rules[goto], 0, xnum, mnum, go, snum) if char == "a"\
                    else calc(rules[goto], 0, xnum, mnum, anum, go)
                    
                return tmp + (calc(rule, index+1, cont, mnum, anum, snum) if char == "x"\
                        else calc(rule, index+1, xnum, cont, anum, snum) if char == "m"\
                        else calc(rule, index+1, xnum, mnum, cont, snum) if char == "a"\
                        else calc(rule, index+1, xnum, mnum, anum, cont))
    return 0


res = calc(rules["in"], 0, (1, 4000), (1, 4000), (1, 4000), (1, 4000))
print(res)

f.close()