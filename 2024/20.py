from utils import *
from collections import defaultdict
import heapq as hq

input_str = open("input.txt", "r").read().strip("\n")
grid, m, n = to_grid(input_str)

def inbound(grid, i, j):
	return 0 <= i < m and 0 <= j < n

def get_start_and_dest(grid):
	start = None
	dest = None
	for i in range(m):
		for j in range(n):
			if start is not None and dest is not None: return start, dest
			if grid[i][j] == "S":
				start = (i, j)
			elif grid[i][j] == "E":
				dest = (i, j)
	return start, dest

def get_costs(start, dest):
	costs = defaultdict(lambda: INF)
	parent = defaultdict(lambda: None)
	heap = [(0, start)]
	costs[start] = 0
	while heap:
		cost, (i, j) = hq.heappop(heap)
		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_i, new_j = i+di, j+dj
			if inbound(grid, new_i, new_j) and grid[new_i][new_j] != "#"\
				and costs[(new_i, new_j)] > (new_cost := cost+1):
				costs[(new_i, new_j)] = new_cost
				parent[(new_i, new_j)] = (i, j)
				hq.heappush(heap, (new_cost, (new_i, new_j)))
	path = []
	current = dest
	while current is not None:
		path.append(current)
		current = parent[current]
	return costs, path

def get_cheats(start, dest, costs, path):
	cheat_costs = defaultdict(lambda: INF)
	heap = [(0, (start, None))]
	cheat_costs[start] = 0
	cheat_adv = dict()
	while heap:
		cost, ((i, j), cheat) = hq.heappop(heap)
		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_i, new_j = i+di, j+dj
			if not inbound(grid, new_i, new_j): continue
			new_cheat = cheat
			if grid[new_i][new_j] == "#":
				if cheat is not None: continue
				else: new_cheat = (new_i, new_j)
			if cheat_costs[(new_i, new_j)] > (new_cost := cost+1):
				if cheat is not None and (new_i, new_j) in path:
					cheat_adv[(i, j)] = costs[(new_i, new_j)]-new_cost
					continue
				cheat_costs[(new_i, new_j)] = new_cost
				hq.heappush(heap, (new_cost, ((new_i, new_j), new_cheat)))
	return cheat_adv

def get_cheats2(costs, path, threshold, cheat_time):
	cheat_adv = []
	opti = costs[path[0]]
	for k in range(len(path)-threshold):
		i, j = path[k]
		for x, y in path[k+threshold:]:
			if (dist := abs(i-x)+abs(j-y)) <= cheat_time:
				cheat_adv.append(opti-costs[(x, y)]-k-dist)
	return cheat_adv

def part1():
	start, dest = get_start_and_dest(grid)
	costs, path = get_costs(start, dest)
	adv = get_cheats(start, dest, costs, set(path))
	final = len(list(filter(lambda x: x >= 100, adv.values())))
	print(final)

def part2():
	start, dest = get_start_and_dest(grid)
	costs, path = get_costs(dest, start)
	adv = get_cheats2(costs, path, 100, 20)
	final = len(list(filter(lambda x: x >= 100, adv)))
	print(final)

part1()
part2()