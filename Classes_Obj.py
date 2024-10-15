class Robot: 
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def into(self): 
        print(f"Robot {self.name} is entering the room")


r1 = Robot("Iron Man", "2.0", 2015)  
r1.into()  

r2 = Robot("Vision", "1.0", 2020)  
r2.into()  

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)