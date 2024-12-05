from utils import *
from collections import defaultdict

input_str = open("input.txt", "r").read().strip("\n")
ordering_str, updates_str = input_str.split("\n\n")

before_dict = defaultdict(set)
after_dict = defaultdict(set)
for line in ordering_str.split("\n"):
	a, b = [int(x) for x in line.split("|")]

	before_dict[a].add(b)
	after_dict[b].add(a)

updates = [list(map(int, line.split(","))) for line in updates_str.split("\n")]


def part1():
	middle_values = []
	for update in updates:
		correct = True
		for i, page in enumerate(update):
			if any([p in after_dict[page] for p in update[i:]]):
				correct = False
				break
		if correct:
			middle_values.append(update[len(update)//2])
	
	print(sum(middle_values))

def part2():
	middle_values = []
	for update in updates:
		correct = True
		for i in range(len(update)):
			for _ in range(10):
				for j in range(i, len(update)):
					if update[j] in after_dict[update[i]]:
						correct = False
						tmp = update[i]
						update[i] = update[j]
						update[j] = tmp
		if not correct:
			middle_values.append(update[len(update)//2])
	
	print(sum(middle_values))

part1()
part2()