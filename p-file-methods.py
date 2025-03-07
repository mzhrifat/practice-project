"""
f=open("test.txt","r")
print(f.read())
f.close()


f=open("test.txt","r")
print(f.fileno())


f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

f=open("myfile.txt","r")
print(f.isatty())

f=open("myfile.txt","r")
print(f.read(33))


f=open("test.txt","r")
print(f.readable())


f=open("test.txt","r")
print(f.readline())
print(f.readline())


f=open("test.txt","r")
print(f.readlines(33))


f=open("myfile.txt","r")
f.seek(4)
print(f.readline())


f=open("myfile.txt","r")
print(f.seekable())


f=open("myfile.txt","r")
print(f.readline())
print(f.tell())


f=open("myfile.txt","a")
f.truncate(20)
f.close()

f=open("myfile.txt","r")
print(f.read())


f=open("myfile.txt","a")
print(f.writable())


#f=open("myfile.txt","a")

#f.close()

f=open("myfile.txt","r")
f.write("see you soon!")
print(f.read)


f = open("myfile.txt", "a")
f.write("\nSee you soon!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())
"""

f=open("myfile.txt","a")
f.writelines(["See you soon","over and out"])
f.close()

#open and read the file after the appending
f=open("myfile.txt","r")
print(f.read())
