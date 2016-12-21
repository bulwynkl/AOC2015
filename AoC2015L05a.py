


'''Imports'''
import os
import string
import re


'''
puzzle
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

condition1:
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.

condition2:
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

condition3:
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.


For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

pseudo code.

import the file as a list of strings

set up some regular expressions...
	if it doesn't match condition 3
		if it matches condition 2
			if it matches condition1
				mark it as nice.
	otherwise it's naughty





'''


filepath='.\L5.txt'

if os.path.isfile(filepath)==True:
	print "found it"
	f = open(filepath,'r')
	norn = f.read().splitlines()	#naughty or nice...
	f.close()
else:
	print "nope"

cond1 = re.compile(r"[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]")	# 3 vowels
cond2 = re.compile(r"([a-zA-Z])\1")	# repeat consecutive letter
cond3 = re.compile('ab|cd|pq|xy')	# not ab, cd, pq, or xy

nice = 0

for i in xrange(len(norn)):
	
	if not cond3.search(norn[i]):
		if cond2.search(norn[i]):
			if cond1.search(norn[i]):
				nice +=1
print nice

