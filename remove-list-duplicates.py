"""
mylist=["a","b","c","a","b","c"]
mylist=list(dict.fromkeys(mylist))
print(mylist)

def my_function(x):
    return list(dict.fromkeys(x))

mylist=my_function(["a","b","c","a","b","c"])
print(mylist)

#reverse a string in python

txt="hello"[::-1]
print(txt)

def my_function(x):
    return x[::-1]

mytxt=my_function("I wonder how this text looks like backwards")

print(mytxt)

"""
#How to Add Two Numbers in Python

x=input("5")
y=input("8")

sum=input(x)+input(y)
print("The sum is :",sum)
