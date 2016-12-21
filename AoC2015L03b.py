import os
import string

'''
pseudo code.

import the string
construct a list.  each member of the list is a tuple consisting of the x,y, and count values.
each new direction increments x and y, and the list checked. if the tuple exists increment the count. If it does not, create a new tuple with that xy set and initiate a count at 1
at the end, the length of the list is the number of houses visited.

 now need to keep track of 2 agents...

'''


filepath='.\L3.txt'

if os.path.isfile(filepath)==True:
	print "found it"
	f = open(filepath,'r')
	data = f.read().splitlines()
	f.close()
	directions = data[0]
#	print directions
else:
	print "nope"

houselist = [[0,0,2]]
Sx = houselist[0][0]
Sy = houselist[0][1]
Rx = Sx
Ry = Sy

print Sx,Sy,Rx,Ry
SantasMove = True

for i in xrange(len(directions)):
	print directions[i]
	print SantasMove
	if SantasMove :
		if directions[i] == "v":		# move down y
			Sy -= 1 	
			print "down Y",Sy
		elif directions[i] == "^" :	# move up y
			Sy += 1
			print "up Y",Sy
		elif directions[i] == ">" :	# move up x
			Sx += 1
			print "up X",Sx
		elif directions[i] == "<" :	# move down x
			Sx -= 1
			print "down X",Sx
		housefound = False
		for j in xrange(len(houselist)):
			if (houselist[j][0] == Sx) and  (houselist[j][1] == Sy) :  # house address matches
				 houselist[j][2] += 1	# increase the present count by one
				 housefound = True
		if housefound == False :
			houselist.append([Sx,Sy,1])
		SantasMove = False
	else :		
		if directions[i] == "v":		# move down y
			Ry -= 1 	
			print "down Y",Ry
		elif directions[i] == "^" :	# move up y
			Ry += 1
			print "up Y",Ry
		elif directions[i] == ">" :	# move up x
			Rx += 1
			print "up X",Rx
		elif directions[i] == "<" :	# move down x
			Rx -= 1
			print "down X",Rx
		housefound = False
		for j in xrange(len(houselist)):
			if (houselist[j][0] == Rx) and  (houselist[j][1] == Ry) :  # house address matches
				 houselist[j][2] += 1	# increase the present count by one
				 housefound = True
		if housefound == False :
			houselist.append([Rx,Ry,1])			
		SantasMove = True	
# print houselist
print len(houselist)

