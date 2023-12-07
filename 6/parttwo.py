import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math

def main():
	data = """Time:      7  15   30
Distance:  9  40  200"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	lines = data.split("\n")
	time = int("".join([num for num in lines[0].strip("Time:").split(" ") if num != ""]))
	Distance = int("".join([num for num in lines[1].strip("Distance:").split(" ") if num != ""]))
	print(time)
	print(Distance)

	possiblebuttonpresstime = []
	for j in range(time):
		distance = j * (time-j)
		if distance > Distance:
			possiblebuttonpresstime.append(j)

	print(len(possiblebuttonpresstime))

if __name__ == '__main__':
	main()