#!/usr/bin/python3

while True:  # Loop to allow multiple calculations
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid number input. Please enter integers only.")

while True:
    operator = input("Enter the operator(+, -, *, /, %): ")
    if operator in ('+', '-', '*', '/', '%'): # Check if the operator is valid
        break
    else:
        print("Invalid Operator. Please enter one of +, -, *, /, %.")

match operator:
    case '+':
        print(f"The sum of both numbers is: {num1 + num2}") # Corrected output message
    case '-':
        print(f"The difference of both numbers is: {num1 - num2}")  # More accurate message
    case '*':
        print(f"The product of both numbers is: {num1 * num2}")  # More accurate message
    case '/':
        if num2 == 0:  # Handle division by zero
            print("Division by zero is not allowed.")
        else:
            print(f"The quotient of both numbers is: {num1 / num2}")  # More accurate message
    case '%':
        print(f"The remainder of both numbers is: {num1 % num2}")  # More accurate message
    case _:  # This case is now unnecessary due to the input validation loop
        pass # This line will never execute, but it's good practice to leave for clarity.

# Offer to continue or exit
while True:
    continue_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_calc == 'yes':
        break  # Go back to the beginning of the outer loop
    elif continue_calc == 'no':
        exit()  # Exit the script
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
