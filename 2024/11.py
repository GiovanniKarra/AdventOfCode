from utils import *

input_str = open("input.txt", "r").read().strip("\n")
stones = list(map(int, input_str.split(" ")))

def blink(stone, times):
	stones = [stone]
	for i in range(times):
		to_insert = []
		for j in range(len(stones)):
			if stones[j] == 0:
				stones[j] = 1
			elif len((s := "%d"%stones[j]))%2 == 0:
				stones[j] = int(s[:len(s)//2])
				to_insert.append((j+1, int(s[len(s)//2:])))
			else:
				stones[j] *= 2024
		for i, (index, val) in enumerate(to_insert):
			stones.insert(index+i, val)
	return stones

def part1():
	final = []
	for stone in stones:
		final += blink(stone, 25)
	print(len(final))

def part2():
	final = []
	for stone in [0]:
		final += blink(stone, 10)
	print(len(final))

part1()
part2()