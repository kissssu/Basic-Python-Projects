#!/usr/bin/python3

#°F = °C × (9/5) + 32

scale = int(input("Type 0 to enter celcius & 1 to enter ferhenit: "))
Temp = int(input("Enter the temp: "))

if (scale == 1):
  print(f"{(Temp - 32) * 5/9} C")
elif (scale == 0):
  print(f"{(Temp * (9/5)) + 32} F")
else:
  print("Error accured! Please try again.")