"""
#fruits=['apple','banana','cherry']
#fruits.append("orange")
a= ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
print (a.append(b))
#print(fruits)


fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)


fruits=fruits = ['apple', 'banana', 'cherry', 'orange']
x=fruits.copy()
print(x)

fruits = ['apple', 'banana', 'cherry', 'orange']
x=fruits.count("cherry")
print(x)


fruits = ['apple', 'banana', 'cherry', 'orange']
cars=['Ford','BMW','Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
x=fruits.index("cherry")
print(x)


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)


fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)


cars=['Ford','Bmw','volvo']
cars.sort(reverse=True)
print(cars)
"""
#A function that returns the length of the value

def myFunc(e):
    return len(e)

cars = ['Ford', 'Mistubishi', 'BMW', 'VW']
cars.sort(key=myFunc)  # ফাংশনকে পাস করতে হবে, কল করা যাবে না।

print(cars)
