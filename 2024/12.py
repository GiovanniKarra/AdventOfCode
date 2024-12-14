from utils import *
from collections import deque


input_str = open("input.txt", "r").read().strip("\n")
grid, m, n = to_grid(input_str)

def get_region_price(i, j):
	type = grid[i][j]
	visited = set()
	visited.add((i, j))
	queue = deque()
	queue.append((i, j))

	perimeter = 0
	area = 1
	while queue:
		i, j = queue.pop()
		for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
			new_i, new_j = i+di, j+dj
			if not (0 <= new_i < m and 0 <= new_j < n):
				perimeter += 1
				continue
			if (new_i, new_j) in visited: continue
			if grid[new_i][new_j] == type:
				queue.append((new_i, new_j))
				visited.add((new_i, new_j))
				area += 1
			else:
				perimeter += 1
	return area*perimeter, visited

def get_region_price_part2(i, j):
	type = grid[i][j]
	visited = set()
	visited.add((i, j))
	queue = deque()
	queue.append((i, j))

	perimeter = 0
	while queue:
		i, j = queue.pop()
		for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
			new_i, new_j = i+di, j+dj
			if not (0 <= new_i < m and 0 <= new_j < n) or (new_i, new_j) in visited: continue
			if grid[new_i][new_j] == type:
				queue.append((new_i, new_j))
				visited.add((new_i, new_j))

	def is_outside(i, j):
		return not (0 <= i < m and 0 <= j < n) or grid[i][j] != type
	for i, j in visited:
		if is_outside(i-1, j) and is_outside(i, j-1):
			perimeter += 1
		if not is_outside(i-1, j) and not is_outside(i, j-1) and is_outside(i-1, j-1):
			perimeter += 1
		if is_outside(i+1, j) and is_outside(i, j-1):
			perimeter += 1
		if not is_outside(i+1, j) and not is_outside(i, j-1) and is_outside(i+1, j-1):
			perimeter += 1
		if is_outside(i+1, j) and is_outside(i, j+1):
			perimeter += 1
		if not is_outside(i+1, j) and not is_outside(i, j+1) and is_outside(i+1, j+1):
			perimeter += 1
		if is_outside(i-1, j) and is_outside(i, j+1):
			perimeter += 1
		if not is_outside(i-1, j) and not is_outside(i, j+1) and is_outside(i-1, j+1):
			perimeter += 1

	return len(visited)*perimeter, visited

def get_all_regions(part=1):
	visited = set()
	total_price = 0
	for i in range(m):
		for j in range(n):
			if (i, j) in visited: continue
			price, new_visited = get_region_price(i, j) if part == 1 else get_region_price_part2(i, j)
			total_price += price
			visited = visited.union(new_visited)
	return total_price

def part1():
	price = get_all_regions()
	print(price)

def part2():
	price = get_all_regions(part=2)
	print(price)

part1()
part2()