import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re

def main():
	data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	lines = data.split("\n")

	total = 0

	for card in lines:
		cardnum = card.split(": ")[0].split(" ")[1]
		cardgameinfo = card.split(": ")[1]

		winningnums = [num for num in cardgameinfo.split(" | ")[0].split(" ") if num != ""]
		gamenums = [num for num in cardgameinfo.split(" | ")[1].split(" ") if num != ""]

		winnumsingame = [num for num in winningnums if num in gamenums]

		parttot = 0
		
		if len(winnumsingame) > 0:
			parttot += 1
			for i in range(len(winnumsingame)-1):
				parttot *= 2

		total += parttot

	print(total)

if __name__ == '__main__':
	main()
