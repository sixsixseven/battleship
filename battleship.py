	#	battleship.py

import os
import random
import time
import sys
import inspect	#	Decomment this line for debugging w/ game_state()

	###	CLASSES (Alphabetical)

class Battleship(object):
	"""Battleship Class definition"""
	#	carrier			Size 5
	#	battleship		Size 4
	#	cruiser			Size 3
	#	destroyer (x2)	Size 2
	#	submarine (x2)	Size 1
	def __init__(self):
		super(Battleship, self).__init__()
		self.shiptype = None
		self.is_sunk = False
		self.size = None
		self.location = None	#	Ships will initially be placed at random. Prevents having to code a "place ship" interface.



class Gameboard(object):
	"""Gameboard Class definition"""
	def __init__(self):
		super(Gameboard, self).__init__()
		self.size = 10
		self.w = "\u2591"	#	░
		self.x = "\u25C8"	#	◈
		self.s = "\u25EF"	#	◯
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
		self.player_name = None
		self.hits = []
		self.misses = []
		self.num_hits = None
		self.num_miss = None
		if self.num_hits and self.miss != None:
			self.hvm = self.num_hits / self.num_miss
		else:
			return None
		self.sunk = None


	###	FUNCTIONS (Alphabetical)

def clear():
	"""Clears the display buffer and resets the title. Better GUI."""
	os.system('clear')
	title()

def game_state():
	print("Player 1")
	print(vars(p1))
	print()
	print("Player 2")
	print(vars(p2))
	throwaway = input("Press Return when ready.")

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
	board = Gameboard()
	#p1 = Battleship()
	p1 = Player()
	#p2 = Battleship()
	p2 = Player()

	game_state()
	#	Create the game objects, and gather the player pertinents.
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