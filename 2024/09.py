from utils import *

input_str = open("input.txt", "r").read().strip("\n")
nums_init = list(map(int, list(input_str)))

def part1():
	nums = nums_init.copy()
	checksum = 0
	index = 0
	back_index = len(nums)-1
	i = 0
	free = False
	while index < back_index:
		while nums[back_index] == 0:
			back_index -= 2
		while nums[index] == 0:
			index += 1
			free = not free
		if back_index < index: break
		if free:
			nums[index] -= 1
			nums[back_index] -= 1
			checksum += (back_index//2)*i
		else:
			nums[index] -= 1
			checksum += (index//2)*i
		i += 1
	print(checksum)

def part2():
	nums = nums_init.copy()
	checksum = 0
	index = 0
	back_index = len(nums)-1
	i = 0
	while index < len(nums):
		free = index%2 == 1
		if free:
			size = nums[index]
			for j in range(back_index, index, -2):
				if 0 < nums[j] <= size:
					ID = j//2
					checksum += ID*(sum(range(i, i+nums[j])))
					i = i+abs(nums[j])
					nums[index] -= nums[j]
					nums[j] = -nums[j]
					break
			if nums[index] == size:
				i += nums[index]
				index += 1
		else:
			ID = index//2
			checksum += ID*(sum(range(i, i+max(0, nums[index]))))
			i = i+abs(nums[index])
			index += 1
	print(checksum)


part1()
part2()