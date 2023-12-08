import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math, collections

def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm



def main():
	data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	instructions = data.split("\n\n")[0]
	mapping = data.split("\n\n")[1].split("\n")

	print(len(instructions))

	lettmap = {}

	locations = []

	for line in mapping:
		
		location = line.split(" = ")[0]
		if location[2] == "A":
			locations.append(location)
		destination = line.split(" = ")[1].split(", ")
		destinationL = destination[0][-3:]
		destinationR = destination[1][:3]


		lettmap[location] = {"L":destinationL,"R":destinationR}

	

	lengths = []

	print(lettmap["ZZZ"][instructions[16697%len(instructions)]])

if __name__ == '__main__':
	main()