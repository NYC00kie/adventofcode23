import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re

def main():
	data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
	with open("./input.txt","r") as fs:
		data = fs.read()

	datalines = data.split("\n")

	symbols = list(dict.fromkeys(re.sub(r"[0-9\.\n]","",data)))

	symreg = r"[\*]"

	# extract symbol spots in the array

	symbolspots = []

	for i,line in enumerate(datalines):

		while re.search(symreg, line):
			spot = re.search(symreg,line).span()[0]
			line = line[:spot] + "." + line[spot+1:]
			symbolspots.append([i,spot])

	data = "\n".join(datalines)
	data = re.sub(symreg,".",data)
	datalines = data.split("\n")
	sepdatalines = [list(x) for x in datalines]



	# make numbers into ints in list

	for i,line in enumerate(datalines):
		while re.search(r"[0-9]+", line):
			search = re.search(r"[0-9]+", line)
			span = search.span()
			match = search.group()
			
			length = span[1]-span[0]

			for j in range(length):
				sepdatalines[i][span[0]+j] = int(match)

			line = line[:span[0]] + "".join(["." for _ in range(length)]) + line[span[1]:]


	# Search pattern
	# . . .
	# . * .
	# . . .

	total_numbers = []

	for spot in symbolspots:
		spot_nums = []
		tl = sepdatalines[spot[0]-1][spot[1]-1]
		tm = sepdatalines[spot[0]-1][spot[1]]
		tr = sepdatalines[spot[0]-1][spot[1]+1]

		ml = sepdatalines[spot[0]][spot[1]-1]
		mm = sepdatalines[spot[0]][spot[1]]
		mr = sepdatalines[spot[0]][spot[1]+1]

		bl = sepdatalines[spot[0]+1][spot[1]-1]
		bm = sepdatalines[spot[0]+1][spot[1]]
		br = sepdatalines[spot[0]+1][spot[1]+1]

		search = [tl,tm,tr,ml,mm,mr,bl,bm,br]

		for thing in search:
			if type(thing) == int and (len(spot_nums) <= 0 or spot_nums[-1] != thing ):
				spot_nums.append(thing)

		# Gear is adjacent to EXACTLY 2 parts

		if len(spot_nums) == 2:
			total_numbers.append(spot_nums[0]*spot_nums[1])

		print(search)

	print(total_numbers)
	print(sum(total_numbers))

main()