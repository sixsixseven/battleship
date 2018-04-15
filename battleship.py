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
	print("\t\tby: sixsixseven\t\tLicense: MIT\n\n\n")

def yesno(i):
	if i == "y" or d == "yes" or d == "ye" or d == "yea" or d == "yeah":
		return True
	elif d == "n" or d == "no" or d == "na" or d == "nah" or d == "nope":
		return False
	else:
		yesno(self)


	###	MAIN
title()

decision = input("Shall we play a game?\nY/N > ").lower()
yesno(decision)

print(decision)