	#	battleship.py

import os

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

x = Battleship()
x.shiptype = "carrier"


class Gameboard(object):
	"""Gameboard Class definition"""
	def __init__(self, arg):
		super(Gameboard, self).__init__()
		self.arg = arg
		self.size = 10
		#	Needs grid/aray of chrs
		#	Use "\u2591" for plain water
		#	Use "\u25C8" for hits
		#	Use "\u25EF" for misses
		#	10x10 GRS. Letters for rows, numbers for columns.
			#	A-J and 1-10. 
		#	Should be generated procedurally and not hard-coded.
			#	Probably in the __init__ section?
		#	Ships will initially be placed at random. Prevents having to code a "place ship" interface.
		#	At BEST, opponests should have up tp a 1% chance of a hit.

class Player(object):
	"""Player Class definition"""
	def __init__(self):
		super(Player, self).__init__()
		#	Needs hits, misses, hit:miss ratio, ships sunk.
		


	###	FUNCTIONS (Alphabetical)

def clear():
	"""Clears the display buffer."""
	os.system('clear')

def hit():
	"""Handles the 'hit' logic."""
	pass

def miss():
	"""Handles the 'miss' logic."""
	pass

def shot():
	"""Handles the logic of shooting a shot."""
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


	###	MAIN
title()

x = yesno("Shall we play a game?")



























