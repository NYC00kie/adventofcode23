import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math, collections




def main():
	data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	instructions = data.split("\n\n")[0]
	mapping = data.split("\n\n")[1].split("\n")

	print(len(instructions))

	lettmap = {}

	for line in mapping:
		
		location = line.split(" = ")[0]
		destination = line.split(" = ")[1].split(", ")
		destinationL = destination[0][-3:]
		destinationR = destination[1][:3]


		lettmap[location] = {"L":destinationL,"R":destinationR}

	i = 0
	location = "AAA"
	while location != "ZZZ":
		location = lettmap[location][instructions[i%len(instructions)]]

		i += 1

	print(i)
	
if __name__ == '__main__':
	main()