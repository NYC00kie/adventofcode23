import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re


#Determin the amount of cubes the games would have been possible with.

def main():

	red = 12
	green = 13
	blue = 14

	data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

	with open("./input.txt","r") as fs:
		data = fs.read()

	data = data.split("\n")
	
	total = 0

	for i,line in enumerate(data):
		stop = False

		# if i > 5:
		# 	break
		game = {
		"red":0,
		"green":0,
		"blue":0
		}
		line = line.replace(f"Game {i+1}: ","")
		tests = [test.split(", ") for test in line.split("; ")]
		print(tests)
		tests = [j for sub in tests for j in sub]
		print(tests)
		for part in tests:
			num = int(part.split(" ")[0])
			if "red" in part and game["red"] < num:
				game["red"] = num

			elif "green" in part and game["green"] < num:
				game["green"] = num

			elif "blue" in part and game["blue"] < num:
				game["blue"]  = num

		total += game["red"] * game["green"] * game["blue"]
			
		print(total)
			
	print(total)



if __name__ == '__main__':
	main()