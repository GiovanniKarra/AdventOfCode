from utils import *
from itertools import product

input_str = open("input.txt", "r").read().strip("\n")
equations = [[int(num.strip(":")) for num in line.split(" ")]
			 for line in input_str.split("\n")]
success_indices = set()

def calculate(terms, operators):
	res = terms[0]
	for i in range(len(operators)):
		if operators[i] == 0: res += terms[i+1]
		elif operators[i] == 1: res *= terms[i+1]
		else: res = int("%d%d"%(res, terms[i+1]))
	return res

def part1():
	count = 0
	for index, equation in enumerate(equations):
		res = equation[0]
		terms = equation[1:]
		operators = product(*[(0, 1) for _ in range(len(terms)-1)])
		for possibility in operators:
			if calculate(terms, possibility) == res:
				count += res
				success_indices.add(index)
				break
	print(count)

def part2():
	count = 0
	for index, equation in enumerate(equations):
		if index in success_indices:
			count += equation[0]
			continue
		res = equation[0]
		terms = equation[1:]
		operators = product(*[(0, 1, 2) for _ in range(len(terms)-1)])
		for possibility in operators:
			if calculate(terms, possibility) == res:
				count += res
				break
	print(count)

part1()
part2()