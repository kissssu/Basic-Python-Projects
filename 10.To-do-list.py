#!/usr/bin/python3

tasks = []

prologue = """Welcome to To-Do list.

Press 1 to enter a task.
Press 2 to remove a task.
Press 3 to mark as completed.
Press q to exit."""

while True:  # Main loop for the to-do list
    print(prologue)  # Print the menu every time

    if tasks: # Check if the list is empty
        for i, task in enumerate(tasks):  # More Pythonic way to iterate with index
            print(f"\t{i + 1}. {task}")

    entered_action = input(f"\n{'=' * 25}\nEnter here: ")
    entered_action = entered_action.lower()

    if entered_action == "1":
        task = input("Enter the task: ")
        tasks.append(task)
    elif entered_action == "2":
        if tasks: # Check if the list is empty
            while True:
                try:
                    removed_task = int(input("Which task you want to remove (enter the task number): "))
                    if 1 <= removed_task <= len(tasks): # Check if the number is in range
                        remove_this_task = tasks.pop(removed_task - 1)
                        print(f"Task '{remove_this_task}' removed.")
                        break
                    else:
                        print("Invalid task number. Please enter a number from the list above.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        else:
            print("No tasks to remove.")

    elif entered_action == "3":
        if tasks: # Check if the list is empty
            while True:
                try:
                    marked_task = int(input("Which task you want to mark (enter the task number): "))
                    if 1 <= marked_task <= len(tasks): # Check if the number is in range
                        tasks[marked_task - 1] += "\t[Done.]"
                        print(f"Task '{tasks[marked_task - 1].replace('\t[Done.]','')}' marked as done.")
                        break
                    else:
                        print("Invalid task number. Please enter a number from the list above.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        else:
            print("No tasks to mark.")

    elif entered_action == "q":
        break  # Exit the loop

    else:
        print("Invalid input. Please enter 1, 2, 3, or q.")
