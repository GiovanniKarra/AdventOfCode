from utils import *
from collections import deque

input_str = open("input.txt", "r").read().strip("\n")
grid = [list(map(int, list(line))) for line in input_str.split("\n")]


def calc_score(i, j):
	queue = deque()
	reached = set()
	visited = set()
	queue.append((i, j))
	while queue:
		y, x = queue.popleft()
		if (y, x) in visited: continue
		visited.add((y, x))
		for dy, dx in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_y, new_x = y+dy, x+dx
			if not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])): continue

			elif grid[new_y][new_x] - grid[y][x] == 1:
				if grid[new_y][new_x] == 9:
					reached.add((new_y, new_x))
				else:
					queue.append((new_y, new_x))
	return len(reached)

def calc_rating(i, j):
	queue = deque()
	rating = 0
	queue.append((i, j))
	while queue:
		y, x = queue.pop()
		for dy, dx in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_y, new_x = y+dy, x+dx
			if not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])): continue

			elif grid[new_y][new_x] - grid[y][x] == 1:
				if grid[new_y][new_x] == 9: rating += 1
				else: queue.append((new_y, new_x))
	return rating

def part1():
	total_score = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				score = calc_score(i, j)
				total_score += score
	print(total_score)

def part2():
	total_rating = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				rating = calc_rating(i, j)
				total_rating += rating
	print(total_rating)

part1()
part2()