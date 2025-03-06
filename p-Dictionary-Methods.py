"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

car={
  "brand":"Ford",
  "model":"Mustang",
  "year":1963
}
x=car.copy()
print(x)

x=('key1','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)


car={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=car.get("price",1500)
print(x)



car={
  "brand":"Ford",
  "model":"jj",
  "year":1960
}
x=car.keys()
print(x)
"""
car={
  "brand":"Ford",
  "model":"jj",
  "year":1960
}
x=car.items()
car["color"]="white"
print(x)

car={
  "brand":"Ford",
  "model":"Mustang",
  "year":1964
}

car.pop("model")
print(car)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.update({"color": "white"})

print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x=car.values()
print(x)
