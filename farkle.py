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
		num = input("Insert the number of players: ")
		try:
			num = int(num)
			if num > 1:
				break
			else:
				print("You can't play alone!")
		except ValueError:
			print("Please insert an integer number.")
	return num

# Control the current hand
def hand_controller(index):
	# Print the active player and generate his hand
    # clear_screen()
    print(f"It's the turn of player n.{index}")
    player_hand = [random.randint(1, 6) for y in range(6)]
    temp_score = 0
    reroll = 1

    while reroll == 1:
        # Print the Hand
        print("Your hand is: ", end=" ")
        for n in player_hand:
            print(n, end=" ")
        print("\n")

        # Ask for the die/dice the player wants to keep
        # and check if it's in the list
        player_input = int(input("Insert the numbers you want to keep: "))
        player_points = 0
        while player_input not in player_hand:
            print("Please insert a number that's in the list.")
            player_input = int(input("Insert the numbers you want to keep: "))

        # Count and add the points
        if player_hand.count(player_input) >= 3 and player_input != 1:
        	temp_score += player_input*100
        	player_hand.remove(player_input)
        	
        elif player_hand.count(player_input) >= 3 and player_input == 1:
            temp_score += player_input*1000 
            player_hand.remove(player_input)
            
        elif player_input == 1:
        	temp_score += 100
        	player_hand.remove(player_input)
        	
        elif player_input == 5:
        	temp_score += 50
        	player_hand.remove(player_input)

        reroll = str(input("Reroll? [Y/n]"))

        if reroll == 'Y' or reroll == 'y':
            reroll = 1
        else:
            reroll = 0

    score[index] += temp_score
    print(score)

# Control Turns
def turn_controller():
    # Loop it for every player
    for x in range(num_players):
        hand_controller(x)

# Setup
clear_screen()
num_players = get_players()

# Start the game
scores = [0 for x in range(num_players)]
turn_controller()

print(scores)
