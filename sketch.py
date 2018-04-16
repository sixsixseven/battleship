import os
os.system('clear')

class Battleship(object):
	"""Battleship Class definition"""
	#	carrier			Size 5
	#	battleship		Size 4
	#	cruiser			Size 3
	#	destroyer 1		Size 2
	#	destroyer 2		Size 2
	#	submarine 1		Size 1
	#	submarine 2		Size 1

	def __init__(self):
		super(Battleship, self).__init__()
		self.shiptype = "carrier"
		self.is_sunk = False
		self.size = 1
		self.location = 3
		self.is_hit = False

	def hit(self):
		shotcount = 0
		print(f"Shots so far: {shotcount}")
		x = int(input("Where would you like to aim? (1-4) > "))
		if x == self.location:
			self.is_sunk = True
			self.is_hit = True
		else:
			os.system('clear')
			shotcount += 1
			print(f"Shots so far: {shotcount}")
			print("You missed. Try Again.")
			



p1 = Battleship()

p1.hit()

print("Game Over.")
print(f"Ship is hit:\t\t{p1.is_hit}")
print(f"Ship is sunk:\t\t{p1.is_sunk}")