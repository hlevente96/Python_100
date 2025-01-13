size = input("Size: S,M,L: ")
pepperoni = input("Pepperoni: y,n: ")
cheese = input("Cheese: y,n: ")

bill = 0
if size == "S":
	bill += 15
elif size == "M":
	bill += 20
else:
	bill += 25

if pepperoni == "y":
	if size == "S":
		bill +=2
	else:
		bill +=3

if cheese == 'y':
	bill += 1

print(f"total bill: ${bill}")