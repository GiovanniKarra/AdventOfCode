from utils import *
from functools import cache

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

@cache
def recursive_blink(stone, times):
	if times == 0: return 1
	
	if stone == 0:
		return recursive_blink(1, times-1)
	elif len((s := "%d"%stone))%2 == 0:
		return recursive_blink(int(s[:len(s)//2]), times-1)+\
			recursive_blink(int(s[len(s)//2:]), times-1)
	else:
		return recursive_blink(stone*2024, times-1)


def part1():
	final = []
	for stone in stones:
		final += blink(stone, 25)
	print(len(final))

def part2():
	final = 0
	for stone in stones:
		final += recursive_blink(stone, 75)
	print(final)

part1()
part2()