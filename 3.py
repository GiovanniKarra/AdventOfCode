f = open("input.txt", "r")
lines = f.readlines()

# PART 1
def get_num_length(line: int, column: int):
    new_col = column
    while new_col < len(lines[line]) and lines[line][new_col].isdigit():
        new_col += 1
    return new_col - column

def is_adj(line: int, column: int, length: int):
    bool_list = []
    bool_list.append(check_symbol(line, column+1))
    bool_list.append(check_symbol(line, column-1))
    bool_list.append(check_symbol(line-1, column-1))
    bool_list.append(check_symbol(line-1, column))
    bool_list.append(check_symbol(line-1, column+1))
    bool_list.append(check_symbol(line+1, column-1))
    bool_list.append(check_symbol(line+1, column))
    bool_list.append(check_symbol(line+1, column+1))
    if True in bool_list:
        return True
    if length > 0:
        return is_adj(line, column+1, length-1)
    return False

def check_symbol(line: int, column: int):
    if line < 0 or column < 0 or line >= len(lines) or column >= len(lines[0]):
        return False
    toret = lines[line][column] not in "0123456789.\n"
    # if toret: print(f"{lines[line][column]} : {toret}")
    return toret


sum = 0
for i in range(len(lines)):
    line = lines[i]
    j = 0
    while j < len(line):
        char = line[j]
        if char.isdigit():
            length = get_num_length(i, j)
            if is_adj(i, j, length-1):
                sum += int(line[j:j+length])
                j += length
        j += 1


# PART 2
def get_adj_nums(line: int, column: int):
    adj = []
    l = ((0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1))
    ind = 0
    while ind < 8:
        yoff = l[ind][0]
        xoff = l[ind][1]
        if lines[line+yoff][column+xoff].isdigit():
            adj.append(l[ind])
            if yoff == 0:
                pass
            else:
                if xoff == -1:
                    ind += 1
                    if yoff != 0 and lines[line+yoff][column].isdigit():
                        ind += 1
                elif xoff == 0:
                    ind += 1
        ind += 1
    if len(adj) == 2:
        num1 = get_num(adj[0][0]+line, adj[0][1]+column)
        num2 = get_num(adj[1][0]+line, adj[1][1]+column)
        #print(f"{num1}*{num2}")
        return num1*num2
    else:
        return 0


def get_num(line: int, column: int):
    num = lines[line][column]
    xoff = 1
    while column+xoff < len(lines[0]):
        if lines[line][column+xoff].isdigit():
            num += lines[line][column+xoff]
            xoff += 1
        else:
            break
    xoff = -1
    while column-xoff >= 0:
        if lines[line][column+xoff].isdigit():
            num = lines[line][column+xoff] + num
            xoff -= 1
        else:
            break
    return int(num)

sum = 0
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        char = line[j]
        if char == "*":
            sum += get_adj_nums(i, j)

print(sum)

f.close()