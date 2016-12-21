
'''
Created on 5Nov.,2016

@author: bulwynkl
'''

'''Imports'''


import os

filepath='.\AoC2015\L1.txt'

if os.path.isfile(filepath)==True:
	print "found it"
	f = open(filepath,'r')
	data = f.read().splitlines()
	f.close()
#	print data[0]
	elevatorlist = data[0]
else:
	print "nope"


floor=0

for i in xrange(len(elevatorlist)):
	
	if elevatorlist[i] == "(":
		floor += 1
	elif elevatorlist[i] == ")":
		floor -= 1
	if floor == -1:
		print "basement"
		print i+1
	
	