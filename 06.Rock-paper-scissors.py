#!/usr/bin/python3

from random import randint

list = ["Rock", "Paper", "Scissors"]
computer_choice = randint(0,2)
your_choice = int(input("Enter your choice(Rock - 0; Paper - 1; Scissors - 2): "))

if computer_choice == your_choice:
  print("It's a tie, try again!")
  
elif your_choice == 0:
  
  if computer_choice == 1:
    print("You lose.")
  
  else:
    print("You won.")
  
elif your_choice == 1:
  
  if computer_choice == 2:
    print("You lose.")
  
  else:
    print("You Won.")
  
elif your_choice == 2:
  
  if computer_choice == 0:
    print("You lose.")
  
  else:
    print("You won.")

else:
  print("Please, check your input.")
  
  
print(f"Computer's choice is {list[computer_choice]}")