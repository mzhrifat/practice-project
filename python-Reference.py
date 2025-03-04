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


a=[1,2,3]
b=["a","b","c"]
print(list(zip(a,b)))

txt="my name is rif"

print(txt.encode(encoding="ascii",errors="backslarshereolace"))



txt="banana"
x=txt.upper()#(20)
print(x)

mydict={83:80}
txt="Hello Sam!"
print(txt.translate(mydict))



txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))


myTuple=("John","peter","Vicky")
x="#".join(myTuple)
print(x)


txt="I could eat bananas all day "
x=txt.partition(("bananas"))
print(x)
"""
txt="THIS IS NOW!"
x=txt.isupper()
print(x)