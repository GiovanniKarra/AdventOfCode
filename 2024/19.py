from utils import *
from functools import cache

input_str = open("input.txt", "r").read().strip("\n")
designs, towels = input_str.split("\n\n")
designs = set(designs.split(", "))
towels = towels.split("\n")

def get_max_design_length(designs):
	max = 0
	for design in designs:
		if (l := len(design)) > max:
			max = l
	return max

@cache
def find_matched_designs(towel, max_length):
	to_check = []
	max_length = min(max_length, len(towel))
	if max_length == 0: return True
	elif max_length == 1: return towel in designs
	for i in range(1, max_length+1):
		if towel[:i] in designs:
			to_check.append(towel[i:])
	return any([find_matched_designs(t, max_length) for t in to_check])

def part1():
	max_length = get_max_design_length(designs)
	possible = sum(find_matched_designs(t, max_length) for t in towels)
	print(possible)

def part2():
	pass

part1()
part2()