
class Vec:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

class Car(Vec):

  def move(self):
    print("Drive!")

class Boat(Vec):

  def move(self):
    print("Sail!")

class Plane(Vec):

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()