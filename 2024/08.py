from utils import *
from collections import defaultdict

input_str = open("input.txt", "r").read().strip("\n")
grid = [list(line) for line in input_str.split("\n")]
m, n = len(grid), len(grid[0])

antennas = defaultdict(list)
for i, line in enumerate(grid):
	for j, chara in enumerate(line):
		if chara == ".": continue
		antennas[chara].append((i, j))

def get_antinodes(a, b):
	diff = (a[0]-b[0], a[1]-b[1])
	return (a[0]+diff[0], a[1]+diff[1]), (b[0]-diff[0], b[1]-diff[1])

def get_antinodes_new(a, b):
	diff = (a[0]-b[0], a[1]-b[1])
	set_a, set_b = set(), set()
	while within_bounds(a):
		set_a.add(a)
		a = (a[0]+diff[0], a[1]+diff[1])
	while within_bounds(b):
		set_b.add(b)
		b = (b[0]-diff[0], b[1]-diff[1])
	return set_a, set_b

def within_bounds(t):
	return 0 <= t[0] < m and 0 <= t[1] < n

def part1():
	visited_loc = set()
	for freq in antennas.keys():
		locations = antennas[freq]
		for i, a in enumerate(locations[:-1]):
			for b in locations[i+1:]:
				for antinode in get_antinodes(a, b):
					if within_bounds(antinode) and antinode not in visited_loc:
						visited_loc.add(antinode)
	print(len(visited_loc))


def part2():
	visited_loc = set()
	for freq in antennas.keys():
		locations = antennas[freq]
		for i, a in enumerate(locations[:-1]):
			for b in locations[i+1:]:
				for antinode in get_antinodes_new(a, b):
					visited_loc |= antinode
	print(len(visited_loc))

part1()
part2()