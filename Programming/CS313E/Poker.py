#  File: Poker.py

#  Description: A program to simulate a game of poker

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428
 
#  Partner's Name: 

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 2/9/16

#  Date Last Modified: 2//16

# ///////////////////////////////////////////////////////////////

import random

class Card (object):
	
	RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
	SUITS = ('C', 'D', 'H', 'S')

	def __init__(self, rank = 12, suit = 'S'):

		if (rank in Card.RANKS):
			self.rank = rank
		else:
			self.rank = 12

		if (suit in Card.SUITS):
			self.suit = suit
		else:
			self.suit = 'S'

	def __str__ (self):

		if (self.rank == 14):
			rank = 'A'
		elif (self.rank == 13):
			rank = 'K'
		elif (self.rank == 12):
			rank = 'Q'
		elif (self.rank == 11):
			rank = 'J'
		else:
			rank = str(self.rank)
		return rank + self.suit

	def __eq__ (self, other):

		return (self.rank == other.rank)

	def __ne__ (self, other):

		return (self.rank != other.rank)

	def __lt__ (self, other):

		return (self.rank < other.rank)

	def __le__ (self, other):

		return (self.rank <= other.rank)

	def __gt__ (self, other):

		return (self.rank < other.rank)

	def __ge__ (self, other):

		return (self.rank <= other.rank)

class Deck (object):

	def __init__(self):

		self.deck = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				card = Card(rank,suit)
				self.deck.append(card)

	def shuffle(self):

		random.shuffle (self.deck)

	def deal (self):

		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)

class Poker (object):

	def __init__ (self, num_players):

		self.deck = Deck()
		self.deck.shuffle()
		self.players = []
		numcards_in_hand = 5

		# populate self.players with empty cells for each player
		for i in range(num_players):
			self.players.append([])

		# round-robin deal
		for i in range(5 * num_players):
			res = i % num_players
			self.players[res].append(self.deck.deal())


	def play(self):

		# create hands for all players
		for i in range (len(self.players)):

			sortedHand = sorted (self.players[i], reverse = True)
			self.players[i] = sortedHand
			hand = ''

			for card in sortedHand:
				hand = hand + str(card) + ' '
			print ('Player ' + str(i + 1) + ": " + hand)

		# generate a matrix to contain info on each player's hand
		points_hand = []

		# loop to calculate score and type of hand for each player
		for i in range(len(self.players)):

			# spot is 2D; spot = [[<hand type>, <score>], ...]
			spot = []

			# Logic tree to figure out which hand player has.
			# The first test it passes will assign and go to next hand			
			if (self.is_royal(self.players[i]) > 0):
				score = self.is_royal(self.players[i])
				spot.append("Royal Flush")
				spot.append(score)

			elif (self.is_straight_flush(self.players[i]) > 0):
				score = self.is_straight_flush(self.players[i])
				spot.append("Straight Flush")
				spot.append(score)

			elif (self.is_four_kind(self.players[i]) > 0):
				score = self.is_four_kind(self.players[i])
				spot.append("Four of a Kind")
				spot.append(score)

			elif (self.is_full_house(self.players[i]) > 0):
				score = self.is_full_house(self.players[i])
				spot.append("Full House")
				spot.append(score)

			elif (self.is_flush(self.players[i]) > 0):
				score = self.is_flush(self.players[i])
				spot.append("Flush")
				spot.append(score)

			elif (self.is_straight(self.players[i]) > 0):
				score = self.is_straight(self.players[i])
				spot.append("Straight")
				spot.append(score)

			elif (self.is_three_kind(self.players[i]) > 0):
				score = self.is_three_kind(self.players[i])
				spot.append("Three of a Kind")
				spot.append(score)

			elif (self.is_two_pair(self.players[i]) > 0):
				score = self.is_two_pair(self.players[i])
				spot.append("Two Pair")
				spot.append(score)

			elif (self.is_one_pair(self.players[i]) > 0):
				score = self.is_one_pair(self.players[i])
				spot.append("One Pair")
				spot.append(score)

			else:
				score = self.is_high_card(self.players[i])
				spot.append("High Card")
				spot.append(score)

			# put the 2-element list into points_hand
			points_hand.append(spot)

		# Prints the type of hand for each player
		print()
		for i in range (len(points_hand)):
			print ('Player ' + str(i + 1) + ": " + str(points_hand[i][0]))

		# loop to figure out which player is the winner		
		win_score = 0
		win_index = 0
		for i in range(len(points_hand)):
			if (points_hand[i][1] > win_score):
				win_score = points_hand[i][1]
				win_index = i + 1

		# prints the winner
		print()
		print ("Player {} wins.".format(win_index))

	'''
	The next few functions test for each individual type of hand.
	The tests will return 0 if it doesn't pass, and return the appropriate
	  value otherwise based on where the special cards are.

	In each type of hand, there will be seperate logic tests catering for
	  each possible composition of the hand.
	  (e.g., three of a kind can be xxxyz, xyyyz, or xyzzz; there will be
	     3 logic tests to figure out if it happened and what the score will be.)

	'''

	def is_royal (self, hand):

		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		rank_order = True
		for i in range (len(hand)):
			rank_order = rank_order and (hand[i].rank == 14 - i)

		if (same_suit and rank_order):
			score = 10 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		else:
			return 0

	def is_straight_flush (self, hand):

		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		rank_order = True
		for i in range (len(hand) - 1):
			rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)

		if (same_suit and rank_order):
			score = 9 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		else:
			return 0


	def is_four_kind (self, hand):

		front_four = True
		back_four = True

		for i in range (len(hand) - 2):
			front_four = front_four and (hand[i].rank == hand[i + 1].rank)

		for i in range (len(hand) - 2):
			back_four = back_four and (hand[i + 1].rank == hand[i + 2].rank)

		if (front_four):
			score = 8 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		elif (back_four):
			score = 8 * (13 ** 5)
			for i in range (len(hand) - 1):
				score += hand[i + 1].rank * (13 ** (4 - i))
			score += hand[i].rank 
			return score
		else:
			return 0

	def is_full_house (self, hand):

		front_trip = True
		back_trip = True

		front_pair = (hand[0].rank == hand[1].rank)
		back_pair = (hand[-1].rank == hand[-2].rank)

		for i in range (len(hand) - 3):
			front_trip = front_trip and (hand[i].rank == hand[i + 1].rank)
			back_trip = back_trip and (hand[i + 2].rank == hand[i + 3].rank)

		if (front_trip and back_pair):
			score = 7 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		elif (front_pair and back_trip):
			score = 7 * (13 ** 5)
			for i in range(len(hand)):
				if ((i + 2) > 4):
					score += hand[i -3].rank * (13 ** (4 - i))
				else:
					score += hand[i + 2].rank * (13 ** (4 - i)) 
			return score
		else:
			return 0


		return ((front_trip and back_pair) or (front_pair and back_trip))

	def is_flush (self, hand):

		same_suit = True
		for i in range(len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		if (same_suit):
			score = 6 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		else:
			return 0

	def is_straight (self, hand):

		rank_order = True
		for i in range(len(hand) - 1):
			rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)

		if (rank_order):
			score = 5 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score
		else:
			return 0


	def is_three_kind (self, hand):

		front_trip = True
		mid_trip = True
		back_trip = True

		for i in range(len(hand) - 3):
			front_trip = front_trip and (hand[i].rank == hand[i + 1].rank)
			mid_trip = mid_trip and (hand[i + 1].rank == hand[i + 2].rank)
			back_trip = back_trip and (hand[i + 2].rank == hand[i + 3].rank)

		if (front_trip):
			score = 4 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score

		elif (mid_trip):
			score = 4 * (13 ** 5)
			for i in range(len(hand ) - 2):
				score += hand[i + 1].rank * (13 ** (4 - i))
			score += hand[0].rank * (13 ** 1)
			score += hand[-1].rank 
			return score

		elif (back_trip):
			score = 4 * (13 ** 5)
			for i in range(len(hand)):
				if ((i + 2) > 4):
					score += hand[i - 3].rank * (13 ** (4 - i))
				else:
					score += hand[i + 2].rank * (13 ** (4 - i))
			return score

		else:
			return 0

	def is_two_pair (self, hand):

		if (hand[0].rank == hand[1].rank):

			if (hand[2].rank == hand[3].rank):
				score = 3 * (13 ** 5)
				for i in range(len(hand)):
					score += hand[i].rank * (13 ** (4 - 1))
				return score

			elif (hand[3].rank == hand[4].rank):
				score = 3 * (13 ** 5)
				for i in range(len(hand) - 1):
					if (i > 1):
						score += hand[i + 1].rank * (13 ** (4 - i))
					else:
						score += hand[i].rank * (13 ** (4 - i))
				score += hand[2].rank
				return score

			else:
				return 0

		elif ((hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)):
			score = 3 * (13 ** 5)
			for i in range(len(hand)):
				if (i == 4):
					score += hand[0].rank
				else:
					score += hand[i + 1].rank * (13 ** (4 - i))
				return score

		else:
			return 0

	def is_one_pair (self, hand):

		if (hand[0].rank == hand[1].rank):
			score = 2 * (13 ** 5)
			for i in range(len(hand)):
				score += hand[i].rank * (13 ** (4 - i))
			return score

		elif (hand[1].rank == hand[2].rank):
			score = 2 * (13 ** 5)
			for i in range(2):
				score += hand[i + 1].rank * (13 ** (4 - i))
			score += hand[0].rank * (13 ** 2)
			score += (hand[3].rank * 13) + hand[4].rank
			return score

		elif (hand[2].rank == hand[3].rank):
			score = 2 * (13 ** 5)
			for i in range(2):
				score += hand[i + 2].rank * (13 ** (4 - i))
			score += hand[0].rank * (13 ** 2)
			score += (hand[1].rank * 13) + hand[4].rank
			return score

		elif (hand[3].rank == hand[4].rank):
			score = 2 * (13 ** 5)
			for i in range(2):
				score += hand[i + 2].rank * (13 ** (4 - i))
			for i in range(len(hand) - 2):
				score += hand[i].rank * (13 ** (2 - i))
			return score

		else:
			return 0

	def is_high_card (self, hand):
		score = 0
		for i in range(len(hand)):
			score += hand[i].rank * (13 ** (4 - i))

		return score


def main():

	print()

	# user-input in range [2, 6]
	num_players = int(input("Enter number of players: "))
	while((num_players < 2) or (num_players > 6)):
		num_players = int(input("Enter number of players: "))
	print()

	# initialize the game
	game = Poker(num_players)

	# play the game
	game.play()

main()

