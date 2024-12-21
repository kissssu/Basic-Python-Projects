#!/usr/bin/python3

opening_scene = '''
\tYou are an adventurer named Kissu, wandering in the vast Forest of Whispers. Rumors say this forest holds a mystical treasure hidden deep within its shadows. However, the journey is perilous, with strange creatures and magical traps guarding the treasure. Armed with only your wits, a torch, and a rusty sword, you step into the forest as the moonlight filters through the dense canopy.'''

scene_1 = '''
- You come across a fork in the path. One path to the left is shrouded in thick mist, and you hear faint whispers, *"Вперёд..."* (Forward...). The path to the right is dimly lit with glowing mushrooms but is eerily silent.

Choices:
1. Take the LEFT path toward the whispers.
2. Take the RIGHT path with the glowing mushrooms.'''

Left = '''
- You venture into the mist, and the whispers grow louder. Suddenly, a spectral figure appears and speaks in a hollow voice, "Prove your courage, mortal." It challenges you to either:
  - Face it in a duel.
  - Answer its riddle.'''

Forward_left_1 = '''
- If you choose the DUEL, the ghostly figure lunges at you. After a fierce battle, you slay it and find a glowing key in its remains. You proceed to the treasure's location but are exhausted. This victory comes at the cost of your strength. (Leads to a challenging finale.)'''

Forward_left_2 = '''
- If you choose the RIDDLE, the figure asks, 
  "I speak without a mouth and hear without ears. What am I?"'''

Riddle_right = '''
If correct, it grants you a map to the treasure, making your journey safer. '''

Riddle_wrong = '''
If incorrect, it curses you, causing you to lose your way.'''

Right = '''
The glowing mushrooms guide you safely. You reach a clearing with an old, abandoned cabin. Inside, you find a dusty journal that mentions a hidden artifact—a protective amulet. However, the cabin feels... off. You must decide:
  - Search for the artifact.
  - Leave immediately.'''

Forward_right_1 = '''
- If you SEARCH, you find the amulet but awaken a shadow creature bound to guard it. You flee, but now the creature follows you. (Leads to a suspenseful finale.)'''

Forward_right_2 = '''
- If you LEAVE, the shadow creature does not awaken, but you lose the chance to gain the amulet. Your journey continues unimpeded but without any magical aid. (Neutral ending.)'''

scene_2 = '''
\tNo matter your previous choices, you eventually find yourself at the Hidden Shrine where the treasure lies. The shrine's doors are locked, and you must use the knowledge, items, or courage you've gathered so far to proceed. Depending on your decisions earlier:'''

ending = [
'''
 - The door opens, and you face one final puzzle to claim the treasure. Solving it leads to the BEST ending, where you retrieve the treasure and escape unharmed''',
'''
- It shields you from the traps inside the shrine, but without the key, you must solve multiple dangerous challenges. (Moderate ending.)''',
'''
- The shrine's defenses overwhelm you, and you perish within. (Bad ending.)''',
'''
- You find the treasure but cannot escape the collapsing shrine, trapped forever. (Tragic ending.)'''
]

def game():
  print(opening_scene)
  print(scene_1)

  choice_1 = input("\nEnter the direction(Right, Left): ")
  if (choice_1.lower() == "left"):

    print(Left)
    answer1 = input("\nDuel or Riddle: ")

    if (answer1.lower() == "duel"):
      print(Forward_left_1)
      print(scene_2)
      print(ending[1])

    elif (answer1.lower() == "riddle"):
      print(Forward_left_2)
      riddle_answer = input("\nAnswer the riddle: ")

      if (riddle_answer.lower() == "echo" or riddle_answer.lower() == "an echo" or riddle_answer.lower() == "a echo"):
        print(Riddle_right)
        print(scene_2)
        print(ending[3])

      else:
        print(Riddle_wrong)
        print(scene_2)
        print(ending[2])
        return

    else:
      print("Invalid direction; Chooce wisely!")
      
  elif (choice_1.lower() == "right"):
    print(Right)
    answer2 = input("\nSearch or Leave: ")

    if (answer2.lower() == "search"):
      print(Forward_right_1)
      print(ending[0])

    elif (answer2.lower() == "leave"):
      print(Forward_right_2)
      print(ending[3])
      return

  else:
    print("Invalid direction; Chooce wisely!")
    return

game()
print("\nThanks for playing the small game.")