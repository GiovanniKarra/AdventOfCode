from functools import cmp_to_key

f = open("input.txt", "r")
lines = f.readlines()

# PART 1
strength = "AKQJT98765432"

def compare(a, b):
    for i in range(5):
        if strength.index(a[i]) == strength.index(b[i]):
            continue
        elif strength.index(a[i]) < strength.index(b[i]):
            return 1
        else:
            return -1
    return 0

hands = {hand: int(bid) for hand, bid in
         [tuple(lines[i].split(" ")) for i in range(len(lines))]}
types = [[] for _ in range(7)]
for hand in hands.keys():
    cards = dict()
    for char in hand:
        if char not in cards.keys():
            cards[char] = 0
        cards[char] += 1

    match len(cards):
        case 1:
            types[0].append(hand)
        case 2:
            if 1 in cards.values():
                types[1].append(hand)
            else:
                types[2].append(hand)
        case 3:
            if 3 in cards.values():
                types[3].append(hand)
            else:
                types[4].append(hand)
        case 4:
            types[5].append(hand)
        case 5:
            types[6].append(hand)

ranks = []
for elem in types:
    if len(elem) == 0:
        continue
    elif len(elem) == 1:
        ranks.append(elem[0])
    else:
        elem.sort(key=cmp_to_key(compare))
        elem.reverse()
        for e in elem:
            ranks.append(e)

sum = 0
rank = len(ranks)
for elem in ranks:
    sum += hands[elem]*rank
    rank -= 1

# PART 2
def add_to_max(cards: dict):
    to_add = cards.pop("J", None)
    if to_add is None:
        return
    elif to_add == 5:
        cards["2"] = 5
        return
    max_key = ""
    max_num = 0
    for char in cards.keys():
        if cards[char] > max_num:
            max_num = cards[char]
            max_key = char
    cards[max_key] += to_add


strength = "AKQT98765432J"

hands = {hand: int(bid) for hand, bid in
         [tuple(lines[i].split(" ")) for i in range(len(lines))]}
types = [[] for _ in range(7)]
for hand in hands.keys():
    cards = dict()
    for char in hand:
        if char not in cards.keys():
            cards[char] = 0
        cards[char] += 1
    add_to_max(cards)

    match len(cards):
        case 1:
            types[0].append(hand)
        case 2:
            if 1 in cards.values():
                types[1].append(hand)
            else:
                types[2].append(hand)
        case 3:
            if 3 in cards.values():
                types[3].append(hand)
            else:
                types[4].append(hand)
        case 4:
            types[5].append(hand)
        case 5:
            types[6].append(hand)

ranks = []
for elem in types:
    if len(elem) == 0:
        continue
    elif len(elem) == 1:
        ranks.append(elem[0])
    else:
        elem.sort(key=cmp_to_key(compare))
        elem.reverse()
        for e in elem:
            ranks.append(e)

sum = 0
rank = len(ranks)
for elem in ranks:
    sum += hands[elem]*rank
    rank -= 1

print(sum)

f.close()