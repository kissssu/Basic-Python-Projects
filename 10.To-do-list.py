#!/usr/bin/python3

tasks = []

prolouge = '''Welcome to To-Do list.

Press 1 to enter a task.
Press 2 remove a task.
Press 3 to mark as completed.
Press q to exit.'''

print(prolouge)
inputed = 0
while (inputed != "q"):
  for i in range(len(tasks)):
    print(f"\t{i+1}. {tasks[i]}")
  Enterd_action = input(f"\n{'='*25}\nEnter here: ")
  inputed = Enterd_action.lower()
  if inputed == "1":
    task = input("Enter the task: ")
    tasks.append(task)
  elif inputed == "2":
    removed_task = int(input("Which task you want to remove(enter the task number): "))
    remove_this_task = tasks.pop(removed_task - 1)
  elif inputed == "3":
    marked_task = int(input("Which task you want to mark(enter the task number): "))
    tasks[marked_task - 1] = tasks[marked_task - 1] + "\t[Done.]"
  else:
    print("Please enter correctly!")  
    