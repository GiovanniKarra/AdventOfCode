f = open("input.txt", "r")
lines = f.readlines()

histories = [[int(elem) for elem in line.split(" ")] for line in lines]

# PART 1
def all_zeros(history):
    for elem in history:
        if elem != 0:
            return False
        
    return True

def create_subhistory(history):
    toret = []
    for i in range(1, len(history)):
        toret.append(history[i]-history[i-1])
    return toret

def create_tree(history):
    toret = []
    current = history
    toret.append(current)
    while not all_zeros(current):
        current = create_subhistory(current)
        toret.append(current)
    return toret

def get_pred(tree):
    pred = 0
    for i in range(len(tree)-2, -1, -1):
        pred = tree[i][-1]+pred
    return pred

sum = 0
for history in histories:
    tree = create_tree(history)
    sum += get_pred(tree)

# PART 2
def get_pred_prev(tree):
    pred = 0
    for i in range(len(tree)-2, -1, -1):
        pred = tree[i][0]-pred
    return pred

sum = 0
for history in histories:
    tree = create_tree(history)
    sum += get_pred_prev(tree)

print(sum)


f.close()