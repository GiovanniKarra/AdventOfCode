from utils import *
import re

input_str = open("input.txt", "r").read()

def part1():
	pattern = r"mul\(\d{0,3},\d{0,3}\)"
	matches = re.findall(pattern, input_str)
	res = 0
	for match in matches:
		nums = re.findall(r"\d{0,3}", match)
		res += product(map(int, filter(lambda n: n != "", nums)))
	print(res)

def part2():
	pattern = r"mul\(\d{0,3},\d{0,3}\)|do\(\)|don't\(\)"
	matches = re.findall(pattern, input_str)
	res = 0
	enabled = True
	for match in matches:
		if match == "do()":
			enabled = True
			continue
		elif match == "don't()":
			enabled = False
			continue
		elif enabled:
			nums = re.findall(r"\d{0,3}", match)
			res += product(map(int, filter(lambda n: n != "", nums)))
	print(res)

part1()
part2()