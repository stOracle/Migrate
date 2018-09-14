#  File: Blackjack.py

#  Description: A program to simulate a game of blackjack

#  Student's Name: Stephen Rauner

#  Student's UT EID: STR428

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 2/15/2016

#  Date Last Modified: 2/17/2016

# ///////////////////////////////////////////////////////////////

import random

class Card (object):
	
	RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
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

		if (self.rank == 1):
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

	def deal (self):

		# if you're out of cards, you can't deal
		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)

class Player (object):

	def __init__ (self, cards):

		# define said player based on the cards fed
		self.cards = cards

	def hit (self, card):

		# if hit is called, it's going to build a card and add it to the self's hand
		self.cards.append(card)

	def get_points (self):

		count = 0
		for card in self.cards:
			if card.rank > 9:
				count += 10
			elif card.rank == 1:
				count += 11
			else:
				count += card.rank

		for card in self.cards:
			if count <= 21:
				break
			elif card.rank == 1:
				count = count - 10

		return count

	def __str__ (self):

		hand = ""
		for i in range (len(self.cards)):
			hand += str(self.cards[i]) + " "

		return "{}- {}".format(hand, self.get_points())

	'''The outcomes of the game (blackjack, winner, tie, lose) are all attributes
	     of the player's hand, thus these methods are under Player, since there
	     isn't a class for hand.'''

	def has_blackjack (self):
		
		return (len(self.cards) == 2) and (self.get_points() == 21)

	# is_winner is dependent on self's hand and how it compares to other's
	def is_winner (self, other):

		# if you didn't bust,
		if (self.get_points() <= 21):
			# but other did, 
			if (other.get_points() > 21):
				# you won
				return True
			# and you have more points than other,
			elif (self.get_points() > other.get_points()):
				# you win
				return True
			# and other has more points (not exceeding 21)
			else:
				# you lose
				return False
		# if you busted
		else:
			# you lost
			return False

	def is_tie (self, other):

		# the second conditional is in case they both busted at the same number		
		return (self.get_points() == other.get_points()) and (self.get_points() <= 21)


class Dealer (Player):

	def __init__ (self, cards):

		Player.__init__ (self, cards)
		self.show_one_card = True

	# over-ride the hit() function in the parent class
	def hit (self, deck):

		self.show_one_card = False
		while self.get_points() < 17:
			self.cards.append(deck.deal())

	def __str__ (self):

		# Only show the first card, ...
		if self.show_one_card:
			return str(self.cards[0])

		# ...until the dealer starts playing.
		else:
			return Player.__str__ (self)


class Blackjack (object):

	def __init__ (self, num_players = 1):

		# make and shuffle the deck
		self.deck = Deck()
		self.deck.shuffle()

		self.num_players = num_players

		# seat_list includes the dealer, player_list does not
		# seat_list is there to assist in round robin dealing
		self.seat_list = []
		self.player_list = []
		for i in range(self.num_players + 1):
			self.seat_list.append([])

		# round robin style of shuffling
		for i in range((self.num_players + 1) * 2):

			# the if statement appends is for the dealer
			if ((i == self.num_players) or (i == 2 * self.num_players + 1)):
				self.seat_list[-1].append(self.deck.deal())
				
			# the else statement is for everyone else
			else:
				res = i % (self.num_players + 1)
				self.seat_list[res].append(self.deck.deal())

			'''Now, self.seat_list is populated with the entire table's hands;
				the last element in self.seatlist is the dealer.'''

		# pick out the players' hands; leave the dealer's
		for i in range(len(self.seat_list) - 1):

			# create the players
			self.player_list.append(Player(self.seat_list[i]))

		# create the dealer
		self.dealer = Dealer(self.seat_list[-1])

		for i in range(len(self.player_list)):
			print ("Player {}: {}".format(i + 1, str(self.player_list[i])))

		print ("Dealer: {}".format(str(self.dealer)))

	def play (self):

		for i in range(self.num_players):

			print()
			points = 0
			while True:

				# if the ith player has a blackjack, they don't get a choice.
				if (self.player_list[i].has_blackjack()):
					print ("Player {} has a blackjack".format(str(i + 1)))
					break

				choice = input('Player {}, you have {} points\nDo you want to hit? [y/n]: \n'
							.format(i + 1, self.player_list[i].get_points()))
				if choice in ('y', 'Y', 'yes'):
					(self.player_list[i]).hit(self.deck.deal())
					points = (self.player_list[i]).get_points()
					print ("Player {}: {}".format(str(i + 1), str(self.player_list[i])))
					if (points >= 21):
						break

				else:
					break

		# once everyone has gone, the dealer plays out his hand
		self.dealer.hit(self.deck)
		print ("\nDealer: {}\n".format(str(self.dealer)))

		for i in range(len(self.player_list)):

			if self.player_list[i].is_winner(self.dealer):
				print ("Player {} wins".format(i + 1))

			elif self.player_list[i].is_tie(self.dealer):
				# push means tie in blackjack
				print ("Player {} pushes".format(i + 1))

			else:
				print ("Player {} loses".format(i + 1))

def main():

	print()

	# user-input in range [1, 6]
	num_players = int(input("Enter number of players: "))

	while((num_players < 1) or (num_players > 6)):
		num_players = int(input("Enter number of players: "))

	print()

	# setup the game
	game = Blackjack(num_players)

	# play the game
	game.play()

main()

