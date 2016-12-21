


'''Imports'''
import os
import string
import re


'''
 a nice string is one with all of the following properties:

 condition1
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

condition2
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

pseudo code.

import the file as a list of strings

set up some regular expressions...
	if it matches condition 1
		if it matches condition 2
			mark it as nice.
	otherwise it's naughty

	condition 1
	([a-zA-Z])\1 twice but without overlapping...
	is overlapping the same as not three?
	i.e. 2 is OK, 3 is not, 4 is OK.

two tests. 
1)
repeated pairs - e.g. xy and xy. 
aaa doesn't count (overlaping) but aaaa does.

2) same letter seperated by a single letter. xax, brb, aaa

both tests need to be true...

final test Condition1 == True and Condition2 = True

String			C1		C2
aa...aa			True	-
aaa				False	True
aaaa			True	True
xy...xy			True	-
xyxy			True	True
x.x				-		True

perhaps walk backwards...

if aaaa:
	C1 = true & C2 = true
test for C2
if x.x :
	C2 = true
else:
	C2 = false # no need to test further - this captures aaa too.
suggests that if we test C2 first, we can eliminate all aaa's where it's false...

new approach.
for each: C2 = false, C1 = false

if x.x :  # ((.)+(.))\1 <don't think this will work.
	C2 = True
	if xy...xy: (([.][.])*([.][.]))\1  or  more likely... ([.][.])\1
		C1 = True
if C1 == True and C2 == True:
	count

str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search('([\w.-]+)@([\w.-]+)', str)
  if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)
	
(.)
for i in range(match.lastindex):
	for j in range(match.lastindex):
		if i != j:
			if match.search(i) == match.search(j):
				C2 = True
match = re()
allmatches = match.findall(stringinput)	
for i in range(len(allmatches)):
	for j in range(len(allmatches)):
		if i != j:
			if allmatches(i) == allmatches(j):
				C2 = True

				lost track of what I'm searching for...
				
r'(a-zA-Z)[a-zA-Z]{1}(?:\1)'
	a letter followed by any single letter, followed by a match for the first letter???
	
r'([.][.])*(?:\1)
any 2 letter combination, separated by zero or more characters, followed by a match of the same pattern???

C2:
[a-zA-Z][a-zA-Z]{1}\1

				
'''


filepath='.\L5.txt'

if os.path.isfile(filepath)==True:
	print "found it"
	f = open(filepath,'r')
	norn = f.read().splitlines()	#naughty or nice...
	f.close()
else:
	print "nope"

cond1 = re.compile(r"([a-zA-Z][a-zA-Z])[a-zA-Z]*\1")	# any pair, repeated
#cond2 = re.compile(r"([a-zA-Z])\1")	# repeat consecutive letter
cond2 = re.compile(r"([a-zA-Z])[a-zA-Z]{1}\1")	# repeat letter with a gap of 1

nice = 0

for i in xrange(len(norn)):
		if cond2.search(norn[i]):
			if cond1.search(norn[i]):
				nice +=1
print nice

