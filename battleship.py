	#	battleship.py



import os



	###	CLASSES (Alphabetical)

class Player(object):
	"""Player Class definition"""
	def __init__(self):
		super(Player, self).__init__()
		


	###	FUNCTIONS (Alphabetical)

def clear():
	os.system('clear')

def title():
	print("\t\t __       ___ ___      __  __         __  ")
	print("\t\t|__)  /\   |   |  |   |_  (_  |__| | |__) ")
	print("\t\t|__) /--\  |   |  |__ |__ __) |  | | |    ")
	print("\t\tby: sixsixseven\t\t    License: MIT\n\n\n")

def yesno(i):
	x = input(f"{i}\nY/N > ").lower()
	
	if x == "y" or x == "yes" or x == "ye" or x == "yea" or x == "yeah":
		return True
	elif x == "n" or x == "no" or x == "na" or x == "nah" or x == "nope":
		return False
	else:
		return yesno(i)


	###	MAIN
title()

x = yesno("Shall we play a game?")




























