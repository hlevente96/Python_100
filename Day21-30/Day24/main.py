with open("Input/Names/invited_names.txt") as f:
    name_list = f.readlines()
for name in name_list:
    with open("Input/Letters/starting_letter.txt") as f:
        letter = f.read().replace("[name]", name.strip())
    with open(f"./Output/invited_{name}.txt","w") as f:
        f.write(letter)
