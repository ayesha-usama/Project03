# -*- coding: utf-8 -*-
"""Project:3 Guess The Number Game Python Project(user).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13M03wyCBIa470BbHpZXUrslYcYnMho1x
"""

import random
secret_number = random.randint(1,100)

while True:
  guess = int(input("Guess a number between 1 and 100:"))

  if guess < secret_number:
    print("Too Low! Guess Higher.")

  elif guess > secret_number:
    print("Too High! Guess Lower.")
  else:
    print("Congratualation! You guessed it right.")
    break