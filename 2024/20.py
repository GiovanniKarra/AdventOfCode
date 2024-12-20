from utils import *
from collections import defaultdict, deque
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
	path = set()
	current = dest
	while current is not None:
		path.add(current)
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

# def get_cheats2(start, dest, costs, path):
# 	cheat_costs = defaultdict(lambda: INF)
# 	index = 0
# 	heap = [(0, (start, 0, index))]
# 	cheat_costs[(start, index)] = 0
# 	cheat_adv = dict()
# 	while heap:
# 		cost, ((i, j), cheat, ind) = hq.heappop(heap)
# 		print((i, j, cheat, ind))
# 		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
# 			new_i, new_j = i+di, j+dj
# 			if not inbound(grid, new_i, new_j): continue
# 			new_cheat = cheat+1 if cheat > 0 else 0
# 			if (cheat >= 20 and (new_i, new_j) in path) or (new_i, new_j) == dest:
# 				cheat_adv[ind] = costs[(new_i, new_j)]-new_cost
# 				continue
# 			if grid[new_i][new_j] == "#":
# 				if cheat >= 19: continue
# 				elif cheat == 0:
# 					new_cheat = 1
# 					index += 1
# 					ind = index
# 			if cheat_costs[((new_i, new_j), ind)] > (new_cost := cost+1):
# 				cheat_costs[((new_i, new_j), ind)] = new_cost
# 				hq.heappush(heap, (new_cost, ((new_i, new_j), new_cheat, ind)))
# 	return cheat_adv

# def get_cheats2(start, dest, costs, path):
# 	cheat_costs = defaultdict(lambda: INF)
# 	heap = [(0, (start, 0))]
# 	cheat_costs[start] = 0
# 	cheat_adv = []
# 	while heap:
# 		cost, ((i, j), cheat) = hq.heappop(heap)
# 		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
# 			new_i, new_j = i+di, j+dj
# 			if not inbound(grid, new_i, new_j): continue
# 			new_cheat = cheat+1 if cheat > 0 else 0
# 			if (cheat >= 20 and (new_i, new_j) in path) or (new_i, new_j) == dest:
# 				cheat_adv.append(costs[(new_i, new_j)]-new_cost)
# 				continue
# 			if grid[new_i][new_j] == "#":
# 				if cheat >= 19: continue
# 				elif cheat == 0: new_cheat = 1
# 			if cheat_costs[(new_i, new_j)] > (new_cost := cost+1):
# 				cheat_costs[(new_i, new_j)] = new_cost
# 				hq.heappush(heap, (new_cost, ((new_i, new_j), new_cheat)))
# 	return cheat_adv

def get_cheats2(start, dest, costs, opti):
	queue = deque()
	queue.append((start, 0, 0))
	visited = set()
	visited.add((start, 0, start))
	cheat_adv = []
	while queue:
		(i, j), cost, cheat = queue.popleft()
		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_i, new_j = i+di, j+dj
			if ((new_i, new_j), cheat, (i, j)) in visited: continue
			new_cost = cost+1
			if not inbound(grid, new_i, new_j): continue
			new_cheat = cheat+1 if cheat > 0 else 0
			if grid[new_i][new_j] == "#":
				if new_cheat >= 20: continue
				elif new_cheat == 0: new_cheat = 1
			elif new_cheat >= 20 or (new_i, new_j) == dest:
				cheat_adv.append(opti-costs[(new_i, new_j)]-new_cost)
				continue
			queue.append(((new_i, new_j), new_cost, new_cheat))
			visited.add(((new_i, new_j), cheat, (i, j)))
	return cheat_adv

def part1():
	start, dest = get_start_and_dest(grid)
	costs, path = get_costs(start, dest)
	adv = get_cheats(start, dest, costs, path)
	final = len(list(filter(lambda x: x >= 100, adv.values())))
	print(final)

def part2():
	start, dest = get_start_and_dest(grid)
	costs, path = get_costs(dest, start)
	adv = get_cheats2(start, dest, costs, costs[start])
	from collections import Counter
	print(sorted(Counter(filter(lambda x: x >= 50, adv)).items()))
	final = len(list(filter(lambda x: x >= 50, adv)))
	print(final)

part1()
part2()