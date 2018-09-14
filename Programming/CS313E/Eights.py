#  File: Eights.py

#  Description: A code to simulate a game of Eights

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 3/8/16

#  Date Last Modified: 3/11/16

# ////////////////////////////////////////////////////////////////////////////////

import random

# ////////////////////////////////////////////////////////////////////////////////

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

# ////////////////////////////////////////////////////////////////////////////////

class Deck (object):

	def __init__(self):

		# create the deck
		self.deck = []

		# fill the deck
		for suit in Card.SUITS:
			for rank in Card.RANKS:

				# create a card
				card = Card(rank,suit)
				# build the deck by adding said card
				self.deck.append(card)

	def shuffle(self):

		random.shuffle (self.deck)

	# checks if the deck is empty
	def empty(self):

		if (len(self.deck) == 0):
			return True
		return False

	def deal (self):

		# if you're out of cards, you can't deal
		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)

# ////////////////////////////////////////////////////////////////////////////////

class Eights (object):

	# initialize the game
	def __init__(self, num_players):
		
		self.deck = Deck()
		self.deck.shuffle()
		self.players = []
		num_cards = 5

		# invent the players
		for i in range(num_players):
			self.players.append([])

		# give the players hands, round-robin style
		for i in range (num_players * num_cards):
			res = i % num_players
			self.players[res].append(self.deck.deal())


	def play (self):

		# Let hte players organize their hands
		for i in range(len(self.players)):

			sortedHand = sorted (self.players[i], reverse = True)
			self.players[i] = sortedHand

		# start off the discard pile with the top card of the deck
		pile = [self.deck.deal()]

		# Turn variable keeps track of which round we are on
		turn = 0

		# Print Round 0
		spec_print(self.players, pile, turn, False)

		# these are the two conditions that stop the game when True
		deck_done = False
		winner = False

		# Keep playing rounds until the deck runs out or we have a winner
		while (not deck_done) and (not winner):

			turn += 1

			# iterates through every player
			for i in range (len(self.players)):

				# at end of hand iteration (j), if no card is played, this will result in a draw
				did_play = False

				# iterates through every card in their hand
				for j in range(len(self.players[i])):

					# checks for eights
					if (self.players[i][j].rank == 8):
						card = self.players[i].pop(j)
						pile.insert(0, card)
						did_play = True
						break

					# next checks suit
					elif (self.players[i][j].suit == pile[0].suit):
						if (self.players[i][j].rank >= pile[0].rank):
							card = self.players[i].pop(j)
							pile.insert(0, card)
							did_play = True
							break
						else:
							card = self.players[i].pop(j)
							pile.insert(0, card)
							did_play = True
							break

					# last checks same rank
					elif (self.players[i][j].rank == pile[0].rank):
						card = self.players[i].pop(j)
						pile.insert(0, card)
						did_play = True
						break

				# once a player runs out of cards, the game is over
				if (len(self.players[i]) == 0):
					winner = True
					break

				# if the player didn't meet one of the requirements for 
				# playing a card, they draw one
				if not did_play:

					# If they try to draw and the deck is empty, the game ends
					if self.deck.empty() == True:
						deck_done = True
						continue
					# if deck is not empty, draw and continue to next player
					self.players[i].append(self.deck.deal())
					continue

			# print round result (once after every player has played or drawn)
			spec_print(self.players, pile, turn, False)

		# print game result once we break from the while loop
		spec_print(self.players, pile, turn, True)

# ////////////////////////////////////////////////////////////////////////////////

# function to calculate the players' scores
def score(hand):
	score = 0
	for card in hand:
		if card.rank > 9:
			score += 10
		elif card.rank == 8:
			score += 50
		else:
			score += card.rank
	return score

# ////////////////////////////////////////////////////////////////////////////////

# function to make the unique print statements
def spec_print(players, discard, turn, is_done):

	if not is_done:

		print ("\nRound {}".format(turn))
		for i in range (len(players)):
			hand = ''
			for card in players[i]:
				hand += "{} ".format(str(card))
			print ("Player {}: {}".format(i + 1, hand))
		pile = ''
		for card in discard:
			pile += "{} ".format(str(card))
		print ("Discard: {}".format(pile))

	else:

		print("\n---------------------------------------------------------")
		print ("\nResult")
		for i in range (len(players)):
			#score = score(players[i])
			
			print ("Player {}: {} points".format(i + 1, score(players[i])))

# ////////////////////////////////////////////////////////////////////////////////

def main():

	num_players = int(input("Enter number of players: "))
	while (num_players < 2) or (num_players > 6):
		num_players = int(input("Enter number of players: "))

	game = Eights(num_players)
	game.play()

main()