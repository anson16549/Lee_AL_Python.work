# what are you trying to compare inside this functions?
# you will need to pass those things in as arguments
# insde the round brackets 
from gameFunctions import winlose, gamea 
def comparechoices(comp, Human):
	if Human == "quit":
		exit()
	elif gamea.computer == Human:
		print("tie! no one wins, Human again")

	elif Human == "rock":
		if gamea.computer == "paper":
			print("You lose!", gamea.computer, "covers", Human, "\n")
			gamea.player_lives = gamea.player_lives - 1
		else:
			print("You win!", Human, "smashes", gamea.computer, "\n")
			gamea.computer_lives = gamea.computer_lives - 1

	elif Human == "paper":
		if gamea.computer == "scissors":
			print("You lose!", gamea.computer, "cuts", Human, "\n")
			gamea.player_lives = gamea.player_lives - 1
		else:
			print("You win!", Human, "covers", gamea.computer, "\n")
			gamea.computer_lives = gamea.computer_lives - 1

	elif Human == "scissors":
		if gamea.computer == "rock":
			print("You lose!", gamea.computer, "smashes", Human, "\n")
			gamea.player_lives = gamea.player_lives - 1
		else:
			print("You win!", Human, "cuts", gamea.computer, "\n")
			gamea.computer_lives = gamea.computer_lives - 1

	else:
		print("That's not a valid choice, try again")