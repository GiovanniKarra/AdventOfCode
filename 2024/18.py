from utils import *
import heapq as hq
from collections import defaultdict

input_str = open("input.txt", "r").read().strip("\n")
positions = [(int(i), int(j)) for i, j in [line.split(",") for line in input_str.split("\n")]]

def inbound(i, j, corrupted):
	return 0 <= i <= 70 and 0 <= j <= 70 and (i, j) not in corrupted

def find_shortest_path(corrupted):
	src = (0, 0)
	dest = (70, 70)
	heap = [src]
	costs = defaultdict(lambda: INF)
	costs[src] = 0
	while heap:
		i, j = hq.heappop(heap)
		cost = costs[(i, j)]
		for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
			new_i, new_j = i+di, j+dj
			if not inbound(new_i, new_j, corrupted): continue
			if costs[(new_i, new_j)] > (new_cost := cost + 1):
				costs[(new_i, new_j)] = new_cost
				hq.heappush(heap, (new_i, new_j))
	return costs[dest]

def part1():
	corrupted = set(positions[:1024])
	print(find_shortest_path(corrupted))

def part2():
	count = len(positions)
	start, end = 0, count
	while len(positions[start:end]) > 1:
		mid = (start+end)//2
		mid_cost = find_shortest_path(set(positions[:mid]))
		if mid_cost < INF:
			start = mid
		else:
			end = mid
	print(positions[start])

part1()
part2()