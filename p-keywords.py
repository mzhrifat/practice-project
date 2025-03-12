"""
x=(5>3 and 5<10)
print(x)


if 5>3 and 5<10:
    print("Both statements are True")
else:
    print("At least one of the statements are False")

import calendar as c
print(c.month_name[6])


x = "welcome"

#if condition returns False, AssertionError is raised:
assert x != "hello", "x should be 'hello'"


for i in range(9):
    if i>3:
        break
        print(i)

i=1
while i<9:
    print(i)
    if i == 3:
        break
        i += 1

class Person:
    name :"Jhon"
    age = 36

p1 = Person()
print(name)

for i in range(9):
    if i == 3:
        continue
        print(i)

i=0
while i<9:
    i += 1
    if i ==3:
        continue
        print(i)

def my_function():
    print("Hello from a function")
my_function()

x ="hello"
del x
print(x)


x= ["apple","banana","cherry"]
del x[0]
print(x)


for i in range (-5,5):
    if i>0:
        print("YES")
    elif i == 0:
      print("WHATEVER")
    else:
       print('NO')


x = 2
if x >3 :
    print("yes")
else:
    print("No")

x=5
try:
    x>10
except:
    print ("Somrething went wrong")
else:
    print("The 'Try' code was executed without raising any errors!")
"""

x= "hello"

try:
    x>3
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You have comparing of different type")



x= 1

try:
    x>10
except NameError:
    print("You have a variable that is not defined.")
except TypeError:
    print("You have comparing of different type")
else:
    print ("The 'Try' code was executed without raising any errors!")
finally:
    print("The try...except block is finished")

