#!/usr/bin/python3

from random import randint

number = randint(0,100)
# print(number)
tries = 0

guess = 0

while (guess != number):
    try:  # Added error handling for invalid input
        guess = int(input("Enter the number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue # Go back to the beginning of the loop

    if (guess < number):
        print("The number is Lesser than the actual number.")
        tries += 1
    elif (guess > number): # Added 'elif' for efficiency
        print("The number is Greater than the actual number.")
        tries += 1
    else: # This 'else' catches the correct guess, avoiding unnecessary iteration
        break # Exit the loop when the number is guessed correctly

print(f"The actual number is {number} & you guessed it in {tries} tries.")
print("Thanks for playing the game.")
