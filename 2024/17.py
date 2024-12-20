from utils import *
import re

input_str = open("input.txt", "r").read().strip("\n")

def get_parsed_data(str):
	registers, program = str.split("\n\n")
	registers = list(map(int, re.findall(r"\d+", registers)))
	program = list(map(int, program.split(" ")[1].split(",")))
	return registers, program

def get_combo_value(combo, registers):
	if 0 <= combo <= 3:
		return combo
	if 4 <= combo <= 6:
		return registers[combo%4]
	else:
		exit(1)

def run_program(registers, program, out):
	pointer = 0
	while pointer < len(program):
		op, arg = program[pointer], program[pointer+1]
		jumped = False
		match op:
			case 0:
				arg = get_combo_value(arg, registers)
				registers[0] //= (2**arg)
			case 1:
				registers[1] ^= arg
			case 2:
				registers[1] = get_combo_value(arg, registers)%8
			case 3:
				if registers[0] != 0:
					pointer = arg
					jumped = True
			case 4:
				registers[1] ^= registers[2]
			case 5:
				out.append(get_combo_value(arg, registers)%8)
			case 6:
				arg = get_combo_value(arg, registers)
				registers[1] = registers[0]//(2**arg)
			case 7:
				arg = get_combo_value(arg, registers)
				registers[2] = registers[0]//(2**arg)
		if not jumped:
			pointer += 2

def part1():
	registers, program = get_parsed_data(input_str)
	out = []
	run_program(registers, program, out)
	print(",".join(map(str, out)))

def part2():
	registers, program = get_parsed_data(input_str)
	init = 100000000000000
	init = 0
	out = []
	while len(out) < len(program):
		out = []
		init += 2
		run_program([init, 0, 0], program, out)
	print(f"{init = }")
	indices = [[] for _ in range(len(program))]
	for i, op in enumerate(program):
		if i == 6: break
		A = init
		while len(indices[i]) < 3:
			init_op = out[i]
			out = []
			run_program([A, 0, 0], program, out)
			if op == out[i] and op != init_op:
				indices[i].append(A)
				# print(f"{op = }, {A = }")
			A += 2
	for k, ind in enumerate(indices):
		print(f"{program[k] = }: ", end="")
		print(f"{ind[0]} + ", end="")
		for i in range(len(ind)-1):
			diff = ind[i+1]-ind[i]
			print("%d "%diff, end="")
		print()

	print(A)

part1()
part2()