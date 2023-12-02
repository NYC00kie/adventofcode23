import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re


#Determin the amount of possible games with 12 red cubes, 13 green cubes, and 14 blue cubes

def main():

	red = 12
	green = 13
	blue = 14

	data = """"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	data = data.split("\n")
	
	total = 0

	for i,line in enumerate(data):
		stop = False

		# if i > 5:
		# 	break

		line = line.replace(f"Game {i+1}: ","")
		tests = [test.split(", ") for test in line.split("; ")]
		print(tests)
		tests = [j for sub in tests for j in sub]
		print(tests)
		for part in tests:

			if "red" in part and int(part.split(" ")[0]) > red:
				stop = True

			if "green" in part and int(part.split(" ")[0]) > green:
				stop = True

			if "blue" in part and int(part.split(" ")[0]) > blue:
				stop = True

		if not stop:
			total += i+1
			
		print(total)
			
	print(total)



if __name__ == '__main__':
	main()