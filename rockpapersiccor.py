# ROCK PAPER SCICCEOR GAME

import random

options = ("rock", "paper", "sciccor")

player = input("Enter your choice: ")

computer = random.choice(options)

print(f"player:{player}")
print(f"computer:{computer}")
