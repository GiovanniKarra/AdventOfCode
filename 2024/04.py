from utils import *

input_str = open("input.txt", "r").read().strip("\n")
grid = [list(line) for line in input_str.split("\n")]
m, n = len(grid), len(grid[0])


def is_xmas(l):
	# print("".join(l)+ ", " + str("".join(l) == "XMAS"))
	return "".join(l) == "XMAS"

def part1():
	occurence_count = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "X":
				if j+3 < n:
					occurence_count += int(is_xmas(grid[i][j:j+4]))
				if j-3 >= 0:
					occurence_count += int(is_xmas(grid[i][j-3:j+1][::-1]))
				if i+3 < m:
					occurence_count += int(is_xmas([grid[k][j] for k in range(i, i+4)]))
				if i-3 >= 0:
					occurence_count += int(is_xmas([grid[k][j] for k in range(i, i-4, -1)]))
				if j+3 < n and i+3 < m:
					occurence_count += int(is_xmas([grid[i+k][j+k] for k in range(0, 4)]))
				if j-3 >= 0 and i+3 < m:
					occurence_count += int(is_xmas([grid[i+k][j-k] for k in range(0, 4)]))
				if j-3 >= 0 and i-3 >= 0:
					occurence_count += int(is_xmas([grid[i-k][j-k] for k in range(0, 4)]))
				if j+3 < n and i-3 >= 0:
					occurence_count += int(is_xmas([grid[i-k][j+k] for k in range(0, 4)]))

	print(occurence_count)


def part2():
	occurence_count = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "A" and 0 < i < m-1 and 0 < j < n-1:
				first_mas = (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or\
					((grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M"))
				second_mas = (grid[i+1][j-1] == "M" and grid[i-1][j+1] == "S") or\
					((grid[i+1][j-1] == "S" and grid[i-1][j+1] == "M"))
				occurence_count += int(first_mas and second_mas)

	print(occurence_count)

part1()
part2()