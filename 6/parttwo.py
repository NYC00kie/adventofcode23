import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math

def main():
	data = """Time:      7  15   30
Distance:  9  40  200"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	lines = data.split("\n")
	Times = [int(num) for num in lines[0].strip("Time:").split(" ") if num != ""]
	Distances = [int(num) for num in lines[1].strip("Distance:").split(" ") if num != ""]
	print(Times)
	print(Distances)
	tots = []
	for i in range(len(Times)):
		time = Times[i]
		possiblebuttonpresstime = []
		for j in range(time):
			distance = j * (time-j)
			if distance > Distances[i]:
				possiblebuttonpresstime.append(j)
		tots.append(len(possiblebuttonpresstime))

	print(math.prod(tots))

if __name__ == '__main__':
	main()