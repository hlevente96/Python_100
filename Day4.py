import random
play = True
while play:
	choices = ["Rock","Paper","Scissors"]
	status = input("Would you like to play? y or n\n").lower()
	if status == "y":
		player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
		machine = random.randint(0,2)
		print(f"Your choice: {choices[player]}, machine choice: {choices[machine]}")
		if player == machine:
			print("Draw")
		elif player == 0:
			if machine == 1:
				print("Loose")
			else:
				print("Win")
		elif player == 1:
			if machine == 0:
				print("Win")
			else:
				print("Loose")
		elif player == 2:
			if machine == 0:
				print("Loose")
			else:
				print("Win")
		else:
			print("Choose different number")
	else:
		play = False