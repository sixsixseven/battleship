	#	battleship.py

import os
import random
import time
import sys

	###	CLASSES (Alphabetical)

class Battleship(object):
	"""Battleship Class definition"""
	#	carrier			Size 5
	#	battleship		Size 4
	#	cruiser			Size 3
	#	destroyer (x2)	Size 2
	#	submarine (x2)	Size 1
	def __init__(self, shiptype, size):
		super(Battleship, self).__init__()
		self.shiptype = shiptype
		self.is_sunk = False
		self.size = size
		self.location = None	#	Ships will initially be placed at random. Prevents having to code a "place ship" interface.

	def getname(self):
		return self.shiptype


class Gameboard(object):
	"""Gameboard Class definition"""
	def __init__(self):
		super(Gameboard, self).__init__()
		self.size = 10
		self.w = "\u2591"	#	░	Water
		self.x = "\u25C8"	#	◈	Hit
		self.s = "\u25EF"	#	◯	Miss
		#	Displays the gameboard, calling to the Player() class to look for hit or miss information.

	def own_board():
		"""Displays own board with ship locations."""
		pass

	def target_board():
		"""Displays targeting board; only shows hits and misses."""
		pass


class Player(object):
	"""Player Class definition"""
	def __init__(self):
		#super(Player, self).__init__()
		self.fleet = []
		self.player_name = None
		self.hits = []
		self.misses = []
		self.num_hits = len(self.hits)	#	Could this just count what's in self.hits?
		self.num_miss = len(self.misses)	#	Could this just count what's in self.misses?
		self.sunk = None
		self.shipyard()
		if self.num_hits and self.miss != 0:
			self.hvm = self.num_hits / self.num_miss


	def shipyard(self):
		self.fleet.append(Battleship('carrier', 5))
		self.fleet.append(Battleship('battleship', 4))
		self.fleet.append(Battleship('cruiser', 3))
		self.fleet.append(Battleship('destroyer', 2))
		self.fleet.append(Battleship('destroyer', 2))
		self.fleet.append(Battleship('submarine', 1))
		self.fleet.append(Battleship('submarine', 1))
			


	###	FUNCTIONS (Alphabetical)

def clear():
	"""Clears the display buffer and resets the title. Better GUI."""
	os.system('clear')
	title()

def game_state():
	"""For debugging. Outputs variable information for specified objects."""
	print("Player 1")
	print(vars(p1))
	print()
	print("Player 2")
	print(vars(p2))
	throwaway = input("Debugging: Press return to continue.")

def shot():
	pass
#	Accept user input for shot placment in the form of "A6, B4, R9"
#	etc. Needs error-checking.

def title():
	"""Displays the title. Should be used on all status screens."""
	print("\t\t __       ___ ___      __  __         __  ")
	print("\t\t|__)  /\   |   |  |   |_  (_  |__| | |__) ")
	print("\t\t|__) /--\  |   |  |__ |__ __) |  | | |    ")
	print("\t\tby: sixsixseven\t\t    License: MIT\n\n\n")

def turn_count():
	"""Handles the current turn count"""
	pass

def turnover():
	"""Handles the player turnover."""
	#	Is a break screen so that opponents can't see each other's screen.
	pass

def yesno(i):
	"""Handles yes/no logic. Accepts exactly 1 string argument in the
	form of a yes/no question."""
	x = input(f"{i}	Y/N > ").lower()
	
	yeslist = ["y", "yes", "ye", "yea", "yeah"]
	nolist = ["n", "no", "na", "nah", "nope"]

	if x in yeslist:
		return True
	elif x in nolist:
		return False
	else:
		return yesno(i)


	###	GAME ENGINE (Main)
gameactive = True
if gameactive == True:
	#	Make the board
	board = Gameboard()

	#	Make the players
	p1 = Player()
	p2 = Player()
	game_state()
	#	Gather the player pertinents.
	clear()
	yn = yesno("Shall we play a game?")
	
	if yn == True:
		clear()
		p1.player_name = input("What is Player One's name? > ").lower()
		
		clear()
		p2.player_name = input("What is Player Two's name? > ").lower()
		yn = None
	else:
		print("Why did you open me, then?\n\n")
		gameactive = False


	#	Decide who goes first.
	clear()
	print("Awesome! I'll pick someone at random to start.\n")
	throwaway = input("Ready Player One and Two? Press Return.")
	
	player_list = [p1.player_name, p2.player_name]
	current_player = random.choice(player_list)
	clear()
	print("Ok. I'm thinking about who I like better:\n")

	for x in range(random.randint(1,10)):	#	Prints suspensful loading dots.
		sys.stdout.write(". ")
		sys.stdout.flush()
		time.sleep(.3)
	print(f"{current_player.title()} gets the first shot!")



else:
	exit(0)