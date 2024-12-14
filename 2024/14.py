from utils import *

input_str = open("input.txt", "r").read().strip("\n")
robots = []
for line in input_str.split("\n"):
	numbers = []
	pos, vel = line.split(" ")
	for num in map(int, pos.split("=")[1].split(",") + vel.split("=")[1].split(",")):
		numbers.append(num)
	robots.append((tuple(numbers[:2]), tuple(numbers[2:])))
width = 101; height = 103

def find_last_pos(robot, time):
	(x, y), (dx, dy) = robot
	x += dx*time
	y += dy*time
	return x%width, y%height

def get_quadrant(x, y):
	if x <= width//2-1:
		if y <= height//2-1:
			return 1
		elif y >= height//2+1:
			return 4
	elif x >= width//2+1:
		if y <= height//2-1:
			return 2
		elif y >= height//2+1:
			return 3
	return 0

def part1():
	quadrants = [0]*5
	for robot in robots:
		x, y = find_last_pos(robot, 100)
		quadrants[get_quadrant(x, y)] += 1
	print(product(quadrants[1:]))

def part2():
	positions = [robot[0] for robot in robots]
	iteration = 0
	looping = True
	while looping:
		iteration += 1
		for i in range(len(robots)):
			positions[i] = find_last_pos((positions[i], robots[i][1]), 1)
		for i in range(len(robots)):
			if positions[i] in positions[:i]: break
			if i == len(robots)-1: looping = False
	print(iteration)

part1()
part2()