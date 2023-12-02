import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re

def main():

	data = ""
	numbers = []
	res = 0
	with open("./input.txt","r") as fs:
		data = fs.read()
		
	#replace all the words for part 2 for the actual numbers
	data = data.replace("oneight","18")
	data = data.replace("fiveight","58")
	data = data.replace("threeight","38")
	data = data.replace("nineight","98")
	data = data.replace("eightwo","82")
	data = data.replace("eighthree","83")
	data = data.replace("twone","21")
	data = data.replace("sevenine","71")
	data = data.replace("one","1")
	data = data.replace("two","2")
	data = data.replace("three","3")
	data = data.replace("four","4")
	data = data.replace("five","5")
	data = data.replace("six","6")
	data = data.replace("seven","7")
	data = data.replace("eight","8")
	data = data.replace("nine","9")


	with open("./input_formatted.txt","w") as fs:
		fs.write(data)

	data = data.split("\n")

	for i,line in enumerate(data):
		numstr = ""

		# if i > 2:
		# 	break

		if not re.search("[0-9]", line):
			continue

		while re.search("[0-9]", line) :
			print(line)
			spot = re.search("[0-9]",line).span()[0]
			numstr += line[spot]
			line = line[:spot] + line[spot+1:]

		print(numstr)
		finalnum = int(f"{numstr[0]+numstr[-1]}")
		numbers.append(finalnum)

	for i in numbers:
		res += i

	print(res)
	

main()




#
#
#
#
#