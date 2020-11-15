# Farkle in Python
# Made by @Pandorolo

# Import
import os
import random

# Clear Screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

# Get Number of Players and check if it's an integer and bigger than 1
def get_players():
	while True:
		num_players = input("Insert the number of players: ")
		try:
			num = int(num_players)
			if num > 1:
				break
			else:
				print("You can't play alone!")
		except ValueError:
			print("Please insert an integer number.")
	return num

# Setup
clear_screen()
get_players()

