"""
mylist=["a","b","c","a","b","c"]
mylist=list(dict.fromkeys(mylist))
print(mylist)
"""
def my_function(x):
    return list(dict.fromkeys(x))

mylist=my_function(["a","b","c","a","b","c"])
print(mylist)