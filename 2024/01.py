import numpy as np
from utils import *

input_str = open("input.txt", "r").read()

def part1():
	lines = input_str.split("\n")
	for line in lines:
		if len(line.split("   ")) < 2: print(line)
	list1, list2 = np.array([(int(x), int(y))
				   for x, y in [line.split("   ") for line in lines]]).transpose()
	list1.sort(); list2.sort()
	final = list1-list2
	distance = np.linalg.norm(final, 1)
	print(int(distance))

def part2():
	lines = input_str.split("\n")
	list1, list2 = np.array([(int(x), int(y))
				   for x, y in [line.split("   ") for line in lines]]).transpose()
	list1.sort(); list2.sort()
	unique, counts = np.unique(list2, return_counts=True)
	occurences = dict(zip(unique, counts))
	similarity = np.array([occurences.get(i, 0) for i in list1])
	score = similarity @ list1
	print(int(score))

# part1()
part2()