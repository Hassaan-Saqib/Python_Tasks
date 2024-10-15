x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x)
print(y)
print(z)
print("\n")
print(type(x))
print(type(y))
print(type(z))
x = float(x)
y = str(z)
z = complex(y)

print(x)
print(y)
print(z)
print("\n")
print(type(x))
print(type(y))
print(type(z))
import random

print(random.randrange(10, 100))