"""
fruits={"apple","banana","cherry"}

fruits.add("orange")
print(fruits)

fruits={"apple","banana","cherry"}
print(fruits)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x &= y & z

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.isdisjoint(y)
print(z)


x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
#z=x.issubset(y)
z=x<=y
print(z)


x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z=x.issuperset(y)
print(z)


fruits={"apple","banana","cherry"}
#fruits.pop()
x=fruits.pop()
print(x)


fruits={"apple","banana","cherry"}
fruits.remove("banana")
print(fruits)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
#z=x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.union(y)
print(z)


x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(x)
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}

x|=y|z
print(x)