

import string
import re
import hashlib

input = "ckczppom"

# test case input = "abcdef609043"



#for i in range(0,100):
for i in range(0,1000000):
#	target = "ckczppom" + format(i,'06d')
#	print target, hashlib.md5(target).hexdigest()
	numberstring = '{:0>6}'.format(i)
	target = input + numberstring
	test = re.compile('^[0]{5,}')
	targetmd5 = hashlib.md5(target).hexdigest()
	if test.match(targetmd5):
		print target, targetmd5, "YAY"
