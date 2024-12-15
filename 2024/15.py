from utils import *

input_str = open("input.txt", "r").read().strip("\n")
grid_str, moves = input_str.split("\n\n")
grid, m, n = to_grid(grid_str)
dir_dict = {
	"^": (-1, 0),
	">": (0, 1),
	"v": (1, 0),
	"<": (0, -1)
}

def get_starting_pos(grid, part=1):
	for i in range(m):
		for j in range(n*part):
			if grid[i][j] == "@":
				return i, j

def move(grid, i, j, dir):
	di, dj = dir_dict[dir]
	new_i, new_j = i+di, j+dj
	if grid[new_i][new_j] == "#":
		return i, j
	if grid[new_i][new_j] == ".":
		grid[i][j] = "."
		grid[new_i][new_j] = "@"
		return new_i, new_j
	while grid[new_i][new_j] == "O":
		new_i += di; new_j += dj
	if grid[new_i][new_j] == "#":
		return i, j
	else:
		grid[new_i][new_j] = "O"
		new_i, new_j = i+di, j+dj
		grid[i][j] = "."
		grid[new_i][new_j] = "@"
		return new_i, new_j

def count_score(grid):
	count = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "O":
				count += i*100+j
	return count

def bigger_grid(grid_str):
	new_grid = [[]]
	index = 0
	for character in grid_str:
		if character == "\n": new_grid.append([]); index += 1
		elif character == "O": new_grid[index].extend("[]")
		elif character == ".": new_grid[index].extend("..")
		elif character == "@": new_grid[index].extend("@.")
		elif character == "#": new_grid[index].extend("##")
	return new_grid

def can_move_box(grid, i, j, di, dj):
	k = None
	if grid[i][j] == "[": k = j+1
	elif grid[i][j] == "]": k = j; j -= 1
	new_i, new_j, new_k = i+di, j+dj, k+dj
	if grid[new_i][new_j] == "#" or grid[new_i][new_k] == "#": return False
	# horizontal
	elif new_j == k or new_k == j:
		if grid[new_i][new_j] == "." or grid[new_i][new_k] == ".":
			return True
		if grid[new_i][new_j] in "[]" and new_j != k:
			return can_move_box(grid, new_i, new_j, di, dj)
		if grid[new_i][new_k] in "[]" and new_k != j:
			return can_move_box(grid, new_i, new_k, di, dj)
	# vertical
	else:
		if grid[new_i][new_j] == "." and grid[new_i][new_k] == ".":
			return True
		can_move = True
		if grid[new_i][new_j] in "[]":
			can_move = can_move and can_move_box(grid, new_i, new_j, di, dj)
		if grid[new_i][new_k] in "[]":
			can_move = can_move and can_move_box(grid, new_i, new_k, di, dj)
		return can_move

def move_box(grid, i, j, di, dj):
	k = None
	if grid[i][j] == "[": k = j+1
	elif grid[i][j] == "]": k = j; j -= 1
	new_i, new_j, new_k = i+di, j+dj, k+dj
	can_move = can_move_box(grid, i, j, di, dj)
	if not can_move: return False
	# horizontal
	elif new_j == k or new_k == j:
		if grid[new_i][new_j] in "[]" and new_j != k:
			move_box(grid, new_i, new_j, di, dj)
		if grid[new_i][new_k] in "[]" and new_k != j:
			move_box(grid, new_i, new_k, di, dj)
	# vertical
	else:
		if grid[new_i][new_j] in "[]":
			move_box(grid, new_i, new_j, di, dj)
		if grid[new_i][new_k] in "[]":
			move_box(grid, new_i, new_k, di, dj)
	grid[i][j] = "."
	grid[i][k] = "."
	grid[new_i][new_j] = "["
	grid[new_i][new_k] = "]"
	return True

def move_bigger(grid, i, j, dir):
	di, dj = dir_dict[dir]
	new_i, new_j = i+di, j+dj
	if grid[new_i][new_j] == "#":
		return i, j
	if grid[new_i][new_j] == ".":
		grid[i][j] = "."
		grid[new_i][new_j] = "@"
		return new_i, new_j
	if grid[new_i][new_j] in "[]":
		can_move = move_box(grid, new_i, new_j, di, dj)
		if can_move:
			grid[i][j] = "."
			grid[new_i][new_j] = "@"
			return new_i, new_j
		else:
			return i, j

def count_score_bigger(grid):
	count = 0
	for i in range(m):
		for j in range(2*n):
			if grid[i][j] == "[":
				count += i*100+j
	return count

def part1():
	grid, _, _ = to_grid(grid_str)
	i, j = get_starting_pos(grid)
	for move_dir in moves:
		if move_dir == "\n": continue
		i, j = move(grid, i, j, move_dir)
	score = count_score(grid)
	print(score)

def part2():
	grid = bigger_grid(grid_str)
	i, j = get_starting_pos(grid, part=2)
	for move_dir in moves:
		if move_dir == "\n": continue
		i, j = move_bigger(grid, i, j, move_dir)
	score = count_score_bigger(grid)
	print(score)

part1()
part2()