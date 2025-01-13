import random

letters_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
letters_large = []
for let in letters_small:
	letters_large.append(let.upper())
letters = letters_small + letters_large

numebers = ['0','1','2',"3","4","5","6",'7','8','9']
symbols = ['(',')','!','@','/','+','*','%','#']

nr_let = int(input('Letters?\n'))
nr_num = int(input('Numbers?\n'))
nr_sym = int(input('Symbols?\n'))

password = []

for let in range(nr_let):
	index = random.randint(0,len(letters)-1)
	password.append(letters[index])

for let in range(nr_num):
	index = random.randint(0,len(numebers)-1)
	password.append(numebers[index])

for let in range(nr_sym):
	index = random.randint(0,len(symbols)-1)
	password.append(symbols[index])
random.shuffle(password)
final_password = ''.join(password)
print(f'Final password is: {final_password}')