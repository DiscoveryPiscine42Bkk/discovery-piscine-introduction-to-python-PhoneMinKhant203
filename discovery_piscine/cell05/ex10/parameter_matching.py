#!/usr/bin/python3
import sys

n = len(sys.argv)
word = "Hello World"

if n == 1 or n > 3:
    print("None")
else:
    print("What was the parameter?", word)
    compare_word = word.lower()
    input_word = sys.argv[1].lower()
    if compare_word == input_word:
        print("Good Job")
    else:
        print("Nope, sorry...")