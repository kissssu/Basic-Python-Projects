#!/usr/bin/python3

import string

text = input("Enter the text: ")

chars = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

def analyser(text):
  char_count = 0
  for i in range(len(text)):
    if text[i] in chars:
      char_count += 1
      
  word_count = 1
  for j in range(len(text)):
    if text[j] == ' ':
      word_count += 1
      
  sentence_count = 0
  for k in range(len(text)):
    if text[k] == '.':
      sentence_count += 1
      
  words = text.split()
  total_length = sum(len(word) for word in words)
  word_counts = len(words)    
  avg_word_length = total_length / word_count
      
  print(f"Text count is {char_count}")
  print(f"There are {word_count} words in the given text.")
  print(f"There are {sentence_count} senteces in the given text.")
  print(f"The average word length in this text is: {avg_word_length}.")
  
analyser(text)