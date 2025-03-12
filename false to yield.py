"""
print (5>6)
print(4 in [1,2,3])

print ("hello" is "goodbye")
print(5==6)
print (5==6 or 6==7)
print(5 ==6 and 6 ==7)
print ("hello" is not "hello")
print(not(5==5))
print(3 not in [1,2,3])


print(5 < 6)

print(2 in [1,2,3])

print(5 is 5)

print(5 == 5)

print(5 == 5 or 6 == 7)

print(5 == 5 and 7 == 7)

print("hello" is not "goodbye")

print(not(5 == 7))

print(4 not in [1,2,3])


for x in range(1,9):
    print(x)

fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)


from datetime import time

x=time(hour=23)
print(x)



#Create a function:
def myfunction():
    global x
    x= "hello"

#execute the function
myfunction()

#x should now be global,and accessible in the global scope.
print(x)

def myfunction():
    global x
    x="kire koi jas tui"

myfunction()
print(x)
"""

x=5
if x > 8:
    print("YEs")
else:
    print("FAlse")

import datetime

x=datetime.datetime.now()
print(x)

fruits=["apple","banana","cherry"]

if "graps" in fruits:
    print("Yes")
else:
    print("False")


x= ["apple","banana","cherry","graps"]

y =["apple","banana","cherry","graps"]
print(x is y)