import os
from collections import defaultdict

os.system('clear')

boardsize = 10

d = defaultdict(int)
for i in range(1,boardsize+1):
	d[i] += 1


w = "\u2591"
x = "\u25C8"
s = "\u25EF"

print(f"Water:	{w}")
print(f"Miss:	{s}")
print(f"Hit:	{x}")
print("")

board = {
		"A1":w, "A2":w, "A3":w,
		"B1":w, "B2":w, "B3":w,
		"C1":w, "C2":w, "C3":w
		}
a = [w,w,w,w,w]


'''
print(" ",1,2,3,4,5,6,7,8,9,10)
print("A",w,w,w,w,w,w,w,w,w,w)
print("B",w,w,w,w,w,w,w,w,w,w)
print("C",w,w,w,w,w,w,w,w,w,w)
print("D",w,w,w,w,w,w,w,w,w,w)
print("E",w,w,w,w,w,w,w,w,w,w)
print("F",w,w,w,w,w,w,w,w,w,w)
print("G",w,w,w,w,w,w,w,w,w,w)
print("H",w,w,w,w,w,w,w,w,w,w)
print("I",w,w,w,w,w,w,w,w,w,w)
print("J",w,w,w,w,w,w,w,w,w,w)
'''
