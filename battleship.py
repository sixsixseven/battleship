	#	battleship.py

import os
import random

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
		self.shiptype = shiptype
		self.is_sunk = is_sunk
		self.size = size
		self.location = location	#	Ships will initially be placed at random. Prevents having to code a "place ship" interface.

	def shot(self):
		pass
	#	Accept user input for shot placment in the form of "A6, B4, R9"
	#	etc. Needs error-checking.


class Gameboard(object):
	"""Gameboard Class definition"""
	def __init__(self, arg):
		super(Gameboard, self).__init__()
		self.arg = arg
		self.size = 10
		self.w = "\u2591"	#	░
		self.x = "\u25C8"	#	◈
		self.s = "\u25EF"	#	◯
		#	Should be generated procedurally and not hard-coded.
			#	Probably in the __init__ section?

		#	At BEST, opponests should have up tp a 1% chance of a hit.


class Player(object):
	"""Player Class definition"""
	def __init__(self):
		super(Player, self).__init__()
		self.player_name = player_name
		self.hits = hits
		self.misses = misses
		self.hvm = hits / misses
		self.sunk = sunk
		


	###	FUNCTIONS (Alphabetical)

def clear():
	"""Clears the display buffer."""
	os.system('clear')

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
	x = input(f"{i}\nY/N > ").lower()
	
	yeslist = ["y", "yes", "ye", "yea", "yeah"]
	nolist = ["n", "no", "na", "nah", "nope"]

	if x in yeslist:
		return True
	elif x in nolist:
		return False
	else:
		return yesno(i)


	###	GAME ENGINE
gameactive = True

if gameactive == True:
	clear()
	title()

	x = yesno("Shall we play a game?")


