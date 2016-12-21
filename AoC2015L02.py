
'''
Created on 5Nov.,2016

@author: bulwynkl
'''

'''Imports'''


import os
import string


filepath='.\L2.txt'

if os.path.isfile(filepath)==True:
	print "found it"
	f = open(filepath,'r')
	rawboxlist = f.read().splitlines()
	f.close()
#	print rawboxlist
else:
	print "nope"

boxlist = []

for i in xrange(len(rawboxlist)):
#	print rawboxlist[i]
#	print string.split(rawboxlist[i],"x")
	boxlist.append(string.split(rawboxlist[i],"x"))
#	print boxlist[i]
	
finalpapersize = 0
finalribbonlength = 0

print (boxlist)

for i in xrange(len(boxlist)):
	x = int(boxlist[i][0])
	y = int(boxlist[i][1])
	z = int(boxlist[i][2])
#	print boxlist[i]
#	print (x,y,z)
	count = 0
	xy = x*y
	xz = x*z
	yz = y*z
	xyz = x*y*z
	papersize = 2*(xy+xz+yz)
	ribbonlength = xyz
	if x >= y and x >= z : 			# X is the biggest number
			papersize += yz 	# don't use X
#			print "X is big", x
			count +=1
			ribbonlength +=2*(y+z)
	elif y > x and y >= z : 
			papersize += xz  	
#			print "Y is big", y
			count += 1
			ribbonlength +=2*(x+z)
	else : 
			papersize += xy  	# don't use Z
#			print "Z is big", z
			count +=1
			ribbonlength += 2*(x+y)
#	print (papersize)
	if count > 1 :
		print "check ", count ,x,y,z
	finalpapersize += papersize
	finalribbonlength += ribbonlength

print "paper area", finalpapersize
print "ribbon length" , finalribbonlength
