import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math, collections




def main():
	data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
	with open("./input.txt","r") as fs:
		data = fs.read()

	instructions = data.split("\n\n")[0]






	
if __name__ == '__main__':
	main()