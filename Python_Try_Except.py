
try:
    print(x)
except NameError:
    print("Var not defined")
except:
    print("Something went wrong")

print("----------------------")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("----------------------")
try:
  print(x)
except:
  print("Something went wrong")
else:
   print("else block")
finally:
  print("The 'try except' is finished")

print("----------------------")
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
print("----------------------")
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
print("----------------------")
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")