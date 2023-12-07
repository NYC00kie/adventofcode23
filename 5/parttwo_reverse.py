import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, threading

def convert_reverse(num,info):

	#
	# num should be the seed number.
	#
	# info should be the convert parameters, looking like this:
	# [[1,2,3],[1,2,3]]
	#
	returnnum = num

	for lines in info:
#		print(f"number: {num} from {lines[1]} ({list(range(lines[1],lines[1]+lines[2]))}), to {lines[0]} ({list(range(lines[0],lines[0]+lines[2]))}) ")
		if num in range(lines[0],lines[0]+lines[2]):
			return num + (lines[1]-lines[0])

			
	return num;

def check(seeds,revmaps,numrange):
	for location in range(numrange[0],numrange[1]):
		teed = location
		if location % 100000 == 0:
			print(location)

		for part in revmaps:
			teed = convert_reverse(teed,part["info"])

		for seedrange in seeds:
			if teed in seedrange:
				print("ALARM ",teed," wird ",location)
				exit()


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

	revmaps = maps[::-1]

	print(revmaps)
	# increase range if no result is returned

	threadnum = 3
	threads = []
	for i in range(threadnum):
		t = threading.Thread(target=check, args=(seeds,revmaps,[i*8000000,(i+1)*8000000],))
		t.start()
		threads.append(t)

	for thread in threads:
		thread.join()

if __name__ == '__main__':
	main()