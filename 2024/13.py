from utils import *
import re
import heapq as hq
from collections import defaultdict
import numpy as np

input_str = open("input.txt", "r").read().strip("\n")
machines_config = input_str.split("\n\n")
machines = []
for config in machines_config:
	machine = []
	pattern = r"\d+"
	numbers = re.findall(pattern, config)
	for i in range(3):
		machine.append((int(numbers[2*i]), int(numbers[2*i+1])))
	machines.append(machine)

def find_shortest_cost(machine):
	a = machine[0]; b = machine[1]; dest = machine[2]
	cost_a = 3; cost_b = 1
	costs = defaultdict(lambda: float("inf"))
	costs[(0, 0)] = 0
	heap = [(0, (0, 0))]
	while heap:
		cost, current = hq.heappop(heap)
		if current == dest: break
		a_step = (current[0]+a[0], current[1]+a[1])
		b_step = (current[0]+b[0], current[1]+b[1])
		if (new_cost := cost + cost_a) < costs[a_step] and a_step[0] <= dest[0] and a_step[1] <= dest[1]:
			costs[a_step] = new_cost
			hq.heappush(heap, (new_cost, a_step))
		if (new_cost := cost + cost_b) < costs[b_step] and b_step[0] <= dest[0] and b_step[1] <= dest[1]:
			costs[b_step] = new_cost
			hq.heappush(heap, (new_cost, b_step))
	return costs[dest] if costs[dest] < float("inf") else 0

def find_shortest_cost_smart(machine):
	a = machine[0]; b = machine[1]; dest = machine[2]
	cost_a = 3; cost_b = 1
	A = np.array([a, b]).T
	b = np.array(dest)
	x = np.linalg.solve(A, b)
	if np.linalg.norm(np.round(x)-x)<1e-4: return cost_a*x[0]+cost_b*x[1]
	else: return 0

def find_shortest_cost_smart2(machine):
	a = machine[0]; b = machine[1]; dest = machine[2]
	cost_a = 3; cost_b = 1
	A = np.array([a, b]).T
	b = np.array(dest)
	x = np.linalg.solve(A, b)
	if np.linalg.norm(np.round(x)-x)<1e-6: return cost_a*x[0]+cost_b*x[1]
	else: return 0

def part1():
	cost = 0
	for machine in machines:
		cost += find_shortest_cost_smart(machine)
	print(cost)

def part2():
	cost = 0
	for machine in machines:
		machine[-1] = (machine[-1][0]+10000000000000, machine[-1][1]+10000000000000)
		cost += find_shortest_cost_smart(machine)
	print(cost)

part1()
part2()