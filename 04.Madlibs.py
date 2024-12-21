#!/usr/bin/python3

# 1. **[ADJECTIVE]** (e.g., "happy," "sparkling")  
ADJECTIVE = input("Enter an ADJECTIVE(Happy, Sparkling): ")
# 2. **[NAME]** (e.g., "Alex," "Luna")  
NAME = input("Enter an Name: ")
# 3. **[EMOTION]** (e.g., "excited," "nervous")  
EMOTION = input("Enter an EMOTION(Excited, Nervous): ")
# 4. **[PLACE]** (e.g., "Everland," "Dreamvale")  
PLACE = input("Enter an PLACE(Everland, Dreamvale): ")
# 5. **[NOUN]** (e.g., "backpack," "wand") (asked multiple times)  
NOUN = input("Enter an NOUN(backpack, wand): ")
# 6. **[ANIMAL]** (e.g., "dragon," "cat")  
ANIMAL = input("Enter an ANIMAL(Dragon, Cat): ")
# 7. **[VERB]** (e.g., "run," "dance") (asked multiple times)  
VERB = input("Enter an VERB(Run, Dance): ")
# 8. **[MAGICAL CREATURE]** (e.g., "unicorn," "phoenix")  
MAGICAL_CREATURE = input("Enter an MAGICAL CREATURE(Phoenix, Unicorn): ")

message = f"""
One bright and {ADJECTIVE} morning, {NAME} woke up feeling {EMOTION}. 
Today was no ordinary day—it was the day they would visit the magical kingdom of {PLACE}. 
After grabbing their trusty {NOUN}, they set off on their {ADJECTIVE} adventure. 

Upon reaching the kingdom, they were greeted by a {ANIMAL} who spoke in a {ADJECTIVE} voice. 
'Welcome to {PLACE}!' the creature said, pointing to a {NOUN} in the distance. 
'You must complete the {VERB} challenge to meet the ruler.'

Determined, {NAME} hurried to the {NOUN} and began to {VERB}. 
After a long and {ADJECTIVE} effort, they finally succeeded. 
The ruler of the kingdom, a {MAGICAL_CREATURE}, appeared and granted them a {NOUN} as a reward.
"""

print(message)