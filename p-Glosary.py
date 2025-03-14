"""
if 5>2:
    print("five is greater than two!")
if 5>2:
    print("Five  is greater than two!")


x=5
y="john"
print(x)
print(y)

x=4
x="salary"
print(x)

x="Jhon"
x='kill'
print(x)

x="awesome"
print("python is" , x)
#string concreation

a="hello"
b="world"
x=a+b
print(x)
"""
#Global variables
x="awesome"

def myfunc():
    print("python is" + x)
myfunc()

def myfunc():
    global x
    x="fantastic"

myfunc()

print("Python is "+ x)