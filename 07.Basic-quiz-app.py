#!/usr/bin/python3

print("Welcome to the quiz.")

questions_list = ['What is the capital of France?', 'Which planet is known as the Red Planet?', 'What is the largest country in the world by land area?', 'Which animal is known as the "Ship of the Desert"?', 'What is the chemical symbol for gold?']
options_list = [['London', 'Paris', 'Berlin', 'Rome'], ['Venus', 'Mars', 'Jupiter', 'Saturn'], ['Russia', 'Canada', 'China', 'United States'], ['Camel', 'Horse', 'Donkey', 'Goat'], ['Ag', 'Au', 'Fe', 'Cu']]
correct_options = [2, 2, 1, 1, 2]

def print_question_and_options(i):
  print(questions_list[i])
  for j in range(4):
    print(f"{j+1}. {options_list[i][j]}")     
    
def check_answer(user_answer, correct_answer, point):
  if user_answer == correct_answer:
    print("You won.")
  else:
    print("Oppps! You're wrong. The Correct answer is", options_list[point][correct_options[point]])

score = 0
for point in range(5):
  print_question_and_options(point)
  answer = int(input("Enter you answer: [1-4]: "))
  check_answer(answer, correct_options[point], point)
  if answer == correct_options[point]:
    score += 1
    
    
print("Your score is:", score)