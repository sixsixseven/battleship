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
		self.shiptype = ""
		self.is_sunk = False
		self.size = 0
		self.location = "Location"	#	Ships will initially be placed at random. Prevents having to code a "place ship" interface.

	def shot(self):
		pass
	#	Accept user input for shot placment in the form of "A6, B4, R9"
	#	etc. Needs error-checking.


class Gameboard(object):
	"""Gameboard Class definition"""
	def __init__(self):
		super(Gameboard, self).__init__()
		self.size = 10
		self.w = "\u2591"	#	░
		self.x = "\u25C8"	#	◈
		self.s = "\u25EF"	#	◯
		#	Displays the gameboard, calling to the Player() class to look for hit or miss information.


class Player(object):
	"""Player Class definition"""
	def __init__(self):
		#super(Player, self).__init__()
		self.player_name = ""
		self.hits = []
		self.misses = []
		self.num_hits = 0
		self.num_miss = 0
		#self.hvm = self.hits / self.misses
		self.sunk = 0
		


	###	FUNCTIONS (Alphabetical)

def clear():
	"""Clears the display buffer and resets the title. Better GUI."""
	os.system('clear')
	title()

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


	###	GAME ENGINE (Main)
gameactive = True

if gameactive == True:
	clear()
	
	yn = yesno("Shall we play a game?")
	if yn == True:
		board = Gameboard()
		p1, p1 = Player(), Battleship()
		p2, p2 = Player(), Battleship()
		
		clear()
		p1.player_name = input("What is Player One's name? > ").lower()
		
		clear()
		p2.player_name = input("What is Player Two's name? > ").lower()

	else:
		print("Why did you open me, then?\n\n")
		exit(0)








