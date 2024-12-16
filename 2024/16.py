from utils import *
from collections import defaultdict
import heapq as hq

input_str = open("input.txt", "r").read().strip("\n")
grid, m, n = to_grid(input_str)

def inbound(grid, i, j):
	if 0 <= i < m and 0 <= j < n:
		return grid[i][j] != "#"
	return False

def get_start_and_dest(grid):
	start = None
	dest = None
	for i in range(m):
		for j in range(n):
			if start is not None and dest is not None: return start, dest
			if grid[i][j] == "S":
				start = ((i, j), (0, 1))
			elif grid[i][j] == "E":
				dest = (i, j)
	return start, dest

def find_smallest_cost(grid, start, dest):
	cost_move = 1; cost_rotate = 1000
	costs = defaultdict(lambda: INF)
	costs[start] = 0
	heap = [(0, start)]
	while heap:
		cost, (position, rotation) = hq.heappop(heap)
		if position == dest:
			costs[position] = cost
			break
		for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
			new_pos = (position[0]+direction[0], position[1]+direction[1])
			if direction == rotation and inbound(grid, new_pos[0], new_pos[1]):
				if (new_cost := cost + cost_move) < costs[(new_pos, direction)]:
					costs[(new_pos, direction)] = new_cost
					hq.heappush(heap, (new_cost, (new_pos, direction)))
			elif direction != rotation:
				if (new_cost := cost + cost_rotate) < costs[(position, direction)]:
					costs[(position, direction)] = new_cost
					hq.heappush(heap, (new_cost, (position, direction)))
	return costs[dest]

def part1():
	grid, m, n = to_grid(input_str)
	start, dest = get_start_and_dest(grid)
	cost = find_smallest_cost(grid, start, dest)
	print(cost)

def part2():
	pass

part1()
part2()