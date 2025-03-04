"""
name=input("Enter your name:Rifat")
print("hello",name)

print(list("hello"))


numbers=[1,2,3]
squard=list(map(lambda x:x**2,numbers))
print(squard)


file=open("test.txt","w")
file=write("hello,world!")
file.close()

#ord

print(ord('A'))

print(pow(2,3))



class parent:
    def greet(self):
        return "Hello From parent"

class child(parent):
    def greet(self):
        return super().greet()+"and child"

print(child().greet())
"""

a=[1,2,3]
b=["a","b","c"]
print(list(zip(a,b)))