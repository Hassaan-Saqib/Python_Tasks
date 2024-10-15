import re

txt="The rain in china 16"
x=re.findall("ai",txt)
print(x)
if x:
  print("YES! We have a match!")
else:
  print("No match")

  """
  Here we have the RegEx module 
  Where we are using different function of re
  """

x=re.findall("[0-9][0-9]",txt)
print(x)
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
x=re.split(" ",txt)
print(x)

x=re.split(" ",txt,1)
print(x)

x=re.sub(" ",'#',txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())
