from utils import *

input_str = open("input.txt", "r").read().strip("\n")
grid = [list(line) for line in input_str.split("\n")]
direction_map = {
	"^": (-1, 0),
	">": (0, 1),
	"v": (1, 0),
	"<": (0, -1)
}
directions = list(direction_map.keys())

def move(g, i, j):
	character = g[i][j]
	di, dj = direction_map[character]
	new_i, new_j = i+di, j+dj
	if not (0 <= new_i < len(g) and 0 <= new_j < len(g[0])):
		g[i][j] = "X"
		return None, None
	
	if g[new_i][new_j] == "#":
		character = directions[(directions.index(character)+1)%4]
		di, dj = direction_map[character]
		new_i, new_j = i+di, j+dj

	g[i][j] = "X"
	g[new_i][new_j] = character

	return new_i, new_j

def better_move(g, i, j, character):
	di, dj = direction_map[character]
	new_i, new_j = i+di, j+dj
	if not (0 <= new_i < len(g) and 0 <= new_j < len(g[0])): return None, None, None
	
	while g[new_i][new_j] == "#":
		character = directions[(directions.index(character)+1)%4]
		di, dj = direction_map[character]
		new_i, new_j = i+di, j+dj

	return new_i, new_j, character

def is_loop(g, guard_i, guard_j, obs_i, obs_j):
	visited_pos = set()
	character = g[guard_i][guard_j]
	g[obs_i][obs_j] = "#"
	visited_pos.add((guard_i, guard_j, character))
	ret = False
	while not ret:
		guard_i, guard_j, character = better_move(g, guard_i, guard_j, character)
		if guard_i is None: break
		elif (guard_i, guard_j, character) in visited_pos: ret = True
		else: visited_pos.add((guard_i, guard_j, character))
	g[obs_i][obs_j] = "."
	return ret

def part1():
	g = grid
	guard_pos = []
	for i in range(len(g)):
		for j in range(len(g[i])):
			if g[i][j] == "^":
				guard_pos = [i, j]
				break
		if guard_pos: break
	init_pos = guard_pos.copy()
	while True:
		guard_pos = list(move(g, guard_pos[0], guard_pos[1]))
		if guard_pos[0] is None:
			break

	print(grid_to_string(g).count("X"))
	g[init_pos[0]][init_pos[1]] = "^"

def part2():
	guard_pos = []
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "^":
				guard_pos = [i, j]
				break
		if guard_pos: break
	
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "X":
				count += int(is_loop(grid, guard_pos[0], guard_pos[1], i, j))

	print(count)


part1()
part2()