alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
	ciper = input("Would you like to use the Cipher? y/n")
	if ciper == 'y':
		code = input('Would you like to encode or decode? e/d')
		if code == 'e':
			message = input("Type your message: ").lower()
			shift = int(input("Type the shift number: "))
			alphabet_shifted = alphabet[shift:] + alphabet[:shift]
		elif code == 'd':
			pass
		else:
			break	
	else:
		break