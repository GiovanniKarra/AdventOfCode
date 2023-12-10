
f = open("input.txt", "r")
lines = f.readlines()
sum = 0

# PART 1
# for line in lines:
#     new_str = ""
#     for char in line.lower():
#         if char not in "abcdefghijklmnopqrstuvwxyz\n":
#             new_str += char

#     if len(new_str) == 1:
#         sum += int(new_str*2)
#     else:
#         print(new_str)
#         sum += int(new_str[0])*10+int(new_str[-1])

# PART 2
sum = 0
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
           "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
for line in lines:
    first = ""
    second = ""
    for i in range(len(line)):
        for number in numbers:
            if line[i:i+len(number)] == number:
                first = number
                break
        if first != "":
            break
    for i in range(len(line), 0, -1):
        for number in numbers:
            if line[i-len(number):i] == number:
                second = number
                break
        if second != "":
            break

    sum += (numbers.index(first)%10)*10 + numbers.index(second)%10
print(sum)
f.close()