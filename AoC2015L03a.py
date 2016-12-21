import os
import string

'''
pseudo code.

import the string
construct a list.  each member of the list is a tuple consisting of the x,y, and count values.
each new direction increments x and y, and the list checked. if the tuple exists increment the count. If it does not, create a new tuple with that xy set and initiate a count at 1
at the end, the length of the list is the number of houses visited.


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

houselist = [[0,0,1]]
x = houselist[0][0]
y = houselist[0][1]
presents = houselist[0][2]

print x,y,presents

for i in xrange(len(directions)):
	print directions[i]
	if directions[i] == "v":		# move down y
		y -= 1 	
		print "down Y",y
	elif directions[i] == "^" :	# move up y
		y += 1
		print "up Y",y
	elif directions[i] == ">" :	# move up x
		x += 1
		print "up X",x
	elif directions[i] == "<" :	# move down x
		x -= 1
		print "down X",x
	housefound = False
	for j in xrange(len(houselist)):
		if (houselist[j][0] == x) and  (houselist[j][1] == y) :  # house address matches
			 houselist[j][2] += 1	# increase the present count by one
			 housefound = True
	if housefound == False :
		houselist.append([x,y,1])
print houselist
print len(houselist)

