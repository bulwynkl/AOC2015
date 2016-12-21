#test

import string
import re
'''
condition2:
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
'''
cond1 = re.compile(r"[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]")	# 3 vowels
string1 = "aabcdpqxuy"
string2 = "acbdpoxqy"
string3 = "dpxq11by"


if cond1.search(string1):
	print string1, " matched"
if cond1.search(string2):
	print string2, " matched"
if cond1.search(string3):
	print string3, " matched"
