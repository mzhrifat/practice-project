"""
#seed
import random
random.seed(10)
print(random.random())

import random
print(random.getstate())
"""

import random
#print a random number:
print(random.random())

#capture the state:
state:random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you capture the state:
print(random.random())