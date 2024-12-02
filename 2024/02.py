from utils import *

input_str = open("input.txt", "r").read()
lines = input_str.split("\n")
reports = [list(map(int, line.split(" "))) for line in lines]

def is_safe(report):
	safe = True
	decreasing = report[0] > report[1]
	break_index = 0
	for i in range(1, len(report)):
		if (report[i] < report[i-1] and not decreasing) or\
			(report[i] > report[i-1] and decreasing) or\
			((diff := abs(report[i]-report[i-1])) < 1 or diff > 3):
			safe = False
			break_index = i
			break
	return safe, break_index

def part1():
	safe_count = 0
	for report in reports:
		if is_safe(report)[0]: safe_count += 1

	print(safe_count)

def part2():
	safe_count = 0
	for report in reports:
		for i in range(len(report)-1):
			safe = is_safe(report[:i]+report[i+1:])[0]
			if safe: break
		if not safe: safe = is_safe(report[:-1])[0]
		safe_count += int(safe)

	print(safe_count)

part1()
part2()