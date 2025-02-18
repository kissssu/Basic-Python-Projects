#!/usr/bin/python3

import random
import string

while True:  # Outer loop for multiple password generations
    while True: # Inner loop for length input validation
        try:
            length = int(input("Enter the password length: "))
            if length > 0:  # Check for positive length
                break
            else:
                print("Password length must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer for the length.")

    chars = string.ascii_letters + string.digits + string.punctuation # Combined in one line


    password = ''.join(random.choice(chars) for i in range(length)) # More efficient way to generate the password

    print(password)

    while True:  # Continue/Exit loop
        generate_again = input("Do you want to generate another password? (yes/no): ").lower()
        if generate_again == 'yes':
            break  # Break out of the generate_again loop to generate a new password
        elif generate_again == 'no':
            exit()  # Exit the entire script
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
