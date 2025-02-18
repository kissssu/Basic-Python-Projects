#!/usr/bin/python3

import string

while True:  # Outer loop for multiple analyses
    text = input("Enter the text (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    chars = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation

    def analyser(text):
        char_count = 0
        word_count = 0  # Initialize word_count to 0
        sentence_count = 0

        for char in text:  # More Pythonic way to iterate through characters
            if char in chars:
                char_count += 1
            elif char in punctuation and char != '.': # Add other punctuations
                char_count +=1

        words = text.split()
        word_count = len(words) # Count words using split()
        
        for char in text:
            if char == '.':
                sentence_count += 1
            #Improved sentence counter
            elif char in ('.','!','?'):
                sentence_count += 1

        total_length = sum(len(word) for word in words)

        if word_count > 0:  # Avoid division by zero
            avg_word_length = total_length / word_count
        else:
            avg_word_length = 0  # Or handle it differently, like printing a message

        print(f"Character count is {char_count}")
        print(f"There are {word_count} words in the given text.")
        print(f"There are {sentence_count} sentences in the given text.")
        print(f"The average word length in this text is: {avg_word_length:.2f}.") # Format to two decimal places

    analyser(text)
