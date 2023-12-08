import numpy as np
import matplotlib.pyplot as plt
import scipy, random, re, math, collections




def main():
	data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
	with open("./input.txt","r") as fs:
		data = fs.read()

#	A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
	rang = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
#	7 Five of a kind, where all five cards have the same label: AAAAA
#	6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#	5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#	4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#	3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#	2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#	1 High card, where all cards' labels are distinct: 23456


# IDEA: restructure the data into integers, so that each individual hand gets its own number (base 16).
# The places 0 - 5 (F00000, the 0) belong to the Cards itself and just get mapped by the standing of each card.
# the 6. place gets decided by the type of hand, four of a kind, full house, and so on.
# this creates a base 16 number thats unique for each unique hand and which will result in a unique decimal number once converted.
# DECIMAL sorting has been solved.

	data = data.split("\n")

	Hands = []

	for line in data:

		Hando = line.split(" ")[0]
		Hand = map(lambda x: rang.index(x), Hando) 

		comphand = collections.deque(Hand)

		counts = {}

		for x in comphand:
			counts[str(x)] = comphand.count(x)

		countvalues = list(counts.values())

		# 5 of a kind
		if len(countvalues) == 1 and 5 in countvalues:
			comphand.appendleft(7)
		#4 of a kind
		elif len(countvalues) == 2 and 4 in countvalues:
			comphand.appendleft(6)
		#full house
		elif len(countvalues) == 2 and 3 in countvalues and 2 in countvalues:
			comphand.appendleft(5)
		#3 of a kind
		elif len(countvalues) == 3 and 3 in countvalues and 1 in countvalues:
			comphand.appendleft(4)
		#Two pair
		elif len(countvalues) == 3 and countvalues.count(2) == 2 and 1 in countvalues:
			comphand.appendleft(3)
		#one pair AA123
		elif len(countvalues) == 4 and countvalues.count(1) == 3 and 2 in countvalues:
			comphand.appendleft(2)
		else:
			comphand.appendleft(1)


		for i in range(len(comphand)):
			comphand[i] = hex(comphand[i]).split("x")[1]
		
		comphand = "".join(comphand)

		comphand = int(comphand,16)

		hand = {"comphand": comphand,"Hand": Hando,"Bet": int(line.split(" ")[1])}

		Hands.append(hand)

	Hands.sort(key=lambda x: x["comphand"])

	total = 0

	for i in range(len(Hands)):
		total += Hands[i]["Bet"] * (i+1)

	print(total)


if __name__ == '__main__':
	main()