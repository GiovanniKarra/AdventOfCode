from utils import *
from collections import defaultdict, deque
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
	parents = defaultdict(list)
	costs[start] = 0
	heap = [(0, start)]
	while heap:
		cost, (position, rotation) = hq.heappop(heap)
		if position == dest:
			costs[position] = min(cost, costs[position])
		for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
			new_pos = (position[0]+direction[0], position[1]+direction[1])
			if direction == rotation and inbound(grid, new_pos[0], new_pos[1]):
				if (new_cost := cost + cost_move) < costs[(new_pos, direction)]:
					costs[(new_pos, direction)] = new_cost
					parents[(new_pos, direction)] = [(position, rotation)]
					hq.heappush(heap, (new_cost, (new_pos, direction)))
				elif new_cost == costs[(new_pos, direction)]:
					costs[(new_pos, direction)] = new_cost
					parents[(new_pos, direction)].append((position, rotation))
					hq.heappush(heap, (new_cost, (new_pos, direction)))
			elif direction != rotation:
				if (new_cost := cost + cost_rotate) < costs[(position, direction)]:
					costs[(position, direction)] = new_cost
					parents[(position, direction)] = [(position, rotation)]
					hq.heappush(heap, (new_cost, (position, direction)))
				elif new_cost == costs[(new_pos, direction)]:
					costs[(new_pos, direction)] = new_cost
					parents[(new_pos, direction)].append((position, rotation))
					hq.heappush(heap, (new_cost, (new_pos, direction)))
	return costs, parents

def part1():
	grid, m, n = to_grid(input_str)
	start, dest = get_start_and_dest(grid)
	costs, _ = find_smallest_cost(grid, start, dest)
	print(costs[dest])

def part2():
	grid, m, n = to_grid(input_str)
	start, dest = get_start_and_dest(grid)
	costs, parents = find_smallest_cost(grid, start, dest)
	visited = set()
	queue = deque()
	for parent in [parents[(dest, (i, j))] for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)) if costs[(dest, (i, j))] == costs[dest]]:
		for p in parent:
			queue.append(p)
	visited_intern = set()
	while queue:
		elem = queue.popleft()
		if elem in visited_intern: continue
		visited.add(elem[0])
		visited_intern.add(elem)
		print()
		print(elem)
		print(parents[elem])
		print()
		for parent in parents[elem]:
			queue.append(parent)
	print(len(visited)+1)

part1()
part2()