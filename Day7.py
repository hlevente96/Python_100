import random

word_list = ['angel', 'balloon', 'camel']
choosen_word = random.choice(word_list)

blank = '_'*len(choosen_word)
print(blank)

life = 5
correct_letters = set()
while True:
	print(f"You have {life} life.")
	guess = input('Guess a letter: ').lower()
	if guess in correct_letters:
		print(f"You have already guessed this letter: {guess}")
	else:
		found = False
		index = 0
		for letter in choosen_word:
			if letter == guess:
				found = True
				blank = list(blank)
				blank[index] = guess
				blank = ''.join(blank)
				correct_letters.add(guess)
			index += 1
		if not found:
			life -= 1
			print(f"The letter {guess} is not in the word")

	if '_' not in blank:
		print(f'You won, the word was: {blank}')
		break
	elif life == 0:
		print(f'Run out of life, the word was: {choosen_word}')
		break
	print(blank)