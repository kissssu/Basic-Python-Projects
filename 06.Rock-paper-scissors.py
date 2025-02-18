#!/usr/bin/python3

from random import randint

options = ["Rock", "Paper", "Scissors"]  # More descriptive variable name

while True:  # Outer loop for multiple games
    while True: # Input validation loop
        try:
            your_choice = int(input("Enter your choice (Rock - 0; Paper - 1; Scissors - 2): "))
            if 0 <= your_choice <= 2: # Check if within valid range
                break
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    computer_choice = randint(0, 2)

    print(f"Computer's choice is {options[computer_choice]}") # Moved this line up for better flow

    if computer_choice == your_choice:
        print("It's a tie, try again!")

    elif your_choice == 0 and computer_choice == 1:
        print("You lose.")
    elif your_choice == 0 and computer_choice == 2:
        print("You win.")
    elif your_choice == 1 and computer_choice == 2:
        print("You lose.")
    elif your_choice == 1 and computer_choice == 0:
        print("You win.")
    elif your_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif your_choice == 2 and computer_choice == 1:
        print("You win.")
    # The else is no longer needed because of the input validation

    while True:  # Continue/Exit loop
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            break  # Break out of the play_again loop to start a new game
        elif play_again == 'no':
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
