# File Not Found
from multiprocessing.managers import Value

try:
    with open("a_file.txt") as f:
        f.read()
    # Attribute Error
    a_dict = {"key":"value"}
    value = a_dict.key2
except FileNotFoundError as e:
    print("File Not Found Error")
    print(f"{e}")
except AttributeError:
    print("Attribute Error")
else:
    print("If no error it will run.")
finally:
    print("Run always")
    #raise TypeError("This is a made up error.")

# Index Error
#fruit_list = [1,2,3]
#fruit_list[3]

# Type Error
#text = "abc"
#print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should be below 3m")
bmi = weight/height**2
print(bmi)
