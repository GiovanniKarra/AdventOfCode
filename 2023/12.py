f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

# PART 1
def get_indices(schema: str):
    toret = []
    for i in range(len(schema)):
        if schema[i] == "?":
            toret.append(i)
    return tuple(toret)

def get_list(schema: str):
    toret = []
    count = 0
    for char in schema:
        if char == "#":
            count += 1
        elif count > 0:
            toret.append(count)
            count = 0
    if count > 0:
        toret.append(count)
    return tuple(toret)

def attempt(bin: int, schema: str, indices: tuple[int], target: tuple[int]):
    cpy = list(schema)
    for i in range(len(indices)):
        ind = indices[i]
        cpy[ind] = "#" if bool((bin >> i)&1) else "."
    # print("".join(cpy))
    return 1 if get_list("".join(cpy)) == target else 0

# sum = 0
# for line in lines:
#     schema, l = line.split(" ")
#     l = tuple(int(elem) for elem in l.split(","))
#     indices = get_indices(schema)
#     for i in range(2**len(indices)):
#         sum += attempt(i, schema, indices, l)


# PART 2
from functools import cache

@cache
def calc_arangements(schema: str, l: tuple[int]):
    schema = schema.lstrip(".")

    if len(l) == 0:
        if all(char != "#" for char in schema):
            return 1
        return 0

    if len(schema) < l[0]:
        return 0
    
    if schema[0] == "#":
        if all(char != "." for char in schema[:l[0]]):
            if len(schema) == l[0]:
                if len(l) > 1:
                    return 0
                return 1
            if schema[l[0]] == "#":
                return 0
            return calc_arangements(schema[l[0]+1:], l[1:])
        return 0
    
    return calc_arangements("#"+schema[1:], l) + calc_arangements(schema[1:], l)

sum = 0
for line in lines:
    schema, l = line.split(" ")
    l = tuple(int(elem) for elem in l.split(","))*5
    schema = "?".join([schema for _ in range(5)])
    sum += calc_arangements(schema, l)

print(sum)

f.close()