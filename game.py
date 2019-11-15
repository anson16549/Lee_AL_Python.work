# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gamea, compare



while gamea.Human is False:
	# set player to True
	print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
	print("Computer lives: ", gamea.computer_lives, "/",gamea.total_lives,"\n")
	print("Human lives: ", gamea.player_lives, "/",gamea.total_lives,"\n")
	print("Choose your weapon!\n")
	print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

	Human = input("choose rock, paper or scissors: ")
	Human = Human.lower()

	print("computer chose ", gamea.computer, "\n")
	print("Human chose ", Human, "\n")

	#### this is where you would call compare
	
	compare.comparechoices(gamea.computer, Human)

	### end compare stuff


	# handle all lives lost for player or AI
	if gamea.player_lives is 0:
		winlose.winorlose("lost")

	elif gamea.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gamea.Human = False
		gamea.computer = gamea.choices[randint(0, 2)]	

