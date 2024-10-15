import module as m
#built in modules
import platform 
m.greeting("ali")

x = platform.system()
print(x)

x = platform.processor()
print(x)

x= dir(platform)
a = m.person1["age"]
print(a)

from module import person1
print(person1["age"])