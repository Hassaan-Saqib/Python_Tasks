import datetime

x = datetime.datetime.now()
print(x)# date complete
print(x.year) # Year
print(x.strftime("%A"))# Day name
print(x.strftime("%B"))# Month Name Full
print(x.strftime("%b"))# Short Month
print(x.strftime("%a"))# Short Day 
print(x.strftime("%w"))#Week Day no
print(x.strftime("%d"))#Month  Day  no
print(x.strftime("%m"))#Month no
print(x.strftime("%y"))#year no
print(x.strftime("%H"))#24 hour
print(x.strftime("%I"))#12 hour
print(x.strftime("%p"))#AM/PM
print(x.strftime("%Z"))#Time Zone
print(x.strftime("%U"))#Week Number
print(x.strftime("%W"))#Week Number
print(x.strftime("%c"))
print(x.strftime("%C"))
print(x.strftime("%x"))#local date
print(x.strftime("%X"))#local time
