#!/usr/bin/python3

from random import randint

number = randint(0,100)
# print(number)
tries = 0

guess = 0

while (guess != number):
  guess = int(input("Enter the number: "))
  if (guess < number):
    print("The number is Lesser than the actual number.")
    tries += 1
  else:
    print("The number is Greater than the actual number.")
    tries += 1

print(f"The actual number is {number} & you guessed it in {tries} tries.")
print("Thanks for playing the game.")
  