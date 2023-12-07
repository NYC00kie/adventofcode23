import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re


def convert(num,info):

	#
	# num should be the seed number.
	#
	# info should be the convert parameters, looking like this:
	# [[1,2,3],[1,2,3]]
	#
	returnnum = num

	for lines in info:
#		print(f"number: {num} from {lines[1]} ({list(range(lines[1],lines[1]+lines[2]))}), to {lines[0]} ({list(range(lines[0],lines[0]+lines[2]))}) ")
		if num in range(lines[1],lines[1]+lines[2]):
			return num + (lines[0]-lines[1])

			
	return num;

def main():
	data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	sections = data.split("\n\n")

	seeds = [int(num) for num in sections[0].strip("seeds: ").split(" ")]
	seeds = [range(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]

	maps = [{"name" : part.split("\n")[0], "info" : [[int(num) for num in nums.split(" ")] for nums in part.split("\n")[1:]]} for part in sections[1:]]

	for mappe in maps:
		mappe["func"] = convert

	minseed = 100000000000000000000000000000
	for seedrange in seeds:
		print(seedrange)
		for seed in seedrange:
			teed = seed
			for part in maps:
				teed = part["func"](teed,part["info"])
			
				

			if teed < minseed :
					minseed = teed

	print(minseed)

if __name__ == '__main__':
	main()
