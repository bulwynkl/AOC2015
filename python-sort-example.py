import random
from operator import itemgetter

def key0(list):
    return list[0]
def key1(list):
    return list[1]
def key2(list):
    return list[2]
def key3(list):
    return list[3]
def key4(list):
    return list[4]
def key5(list):
    return list[5]
def key6(list):
    return list[6]
def key7(list):
    return list[7]
def key8(list):
    return list[8]
def key9(list):
    return list[9]
#'''  
#make an array
boxofgoodies = [[random.randint(1, 100) for i in range(10)] for j in range(1000)]
#'''


for i in range(len(boxofgoodies)):
    print boxofgoodies[i]
print " "
for i in range(len(boxofgoodies)):
    print sorted(boxofgoodies, key=key9)[i]
print " "
for i in range(len(boxofgoodies)):
    print sorted(boxofgoodies, key=key0, reverse=True)[i]    
print " "
boxofgoodies.sort(key=key2, reverse=True)
for i in range(len(boxofgoodies)):
    print boxofgoodies[i]
print " "

for i in range(len(boxofgoodies)):
	print sorted(boxofgoodies, key=itemgetter(0,2,9))[i]
	

print sorted(boxofgoodies, key=key1)
print sorted(boxofgoodies, key=key2)
print sorted(boxofgoodies, key=key3)
print sorted(boxofgoodies, key=key4)
print sorted(boxofgoodies, key=key5)
print sorted(boxofgoodies, key=key6)
print sorted(boxofgoodies, key=key7)
print sorted(boxofgoodies, key=key8)
print sorted(boxofgoodies, key=key9)
#print boxofgoodies
