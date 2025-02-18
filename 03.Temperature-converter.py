#!/usr/bin/python3

while True:  # Outer loop for multiple conversions
    while True: # Inner loop for scale input validation
        try:
            scale = int(input("Type 0 to enter Celsius & 1 to enter Fahrenheit: "))
            if scale in (0, 1): # Check if scale is valid
                break
            else:
                print("Invalid scale. Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter an integer (0 or 1).")

    while True: # Inner loop for temperature input validation
        try:
            temp = float(input("Enter the temperature: ")) # Use float for temperatures
            break
        except ValueError:
            print("Invalid temperature input. Please enter a number.")

    if scale == 1:
        celsius = (temp - 32) * 5/9
        print(f"{celsius:.2f} C") # Format to two decimal places
    elif scale == 0:
        fahrenheit = (temp * (9/5)) + 32
        print(f"{fahrenheit:.2f} F") # Format to two decimal places

    while True: # Loop for continue/exit prompt
        continue_calc = input("Do you want to perform another conversion? (yes/no): ").lower()
        if continue_calc == 'yes':
            break  # Go back to the beginning of the outer loop
        elif continue_calc == 'no':
            exit()  # Exit the script
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
