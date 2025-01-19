
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#{"A": "Alfa", "B": "Bravo"}
#df = pd.read_csv("nato_phonetic_alphabet.csv")

#letter_codes = {row.letter: row.code for (index, row) in df.iterrows()}
#print(letter_codes)
#
##TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#word = input("Tell me a word: ")
#codes = [letter_codes[letter.upper()] for letter in word]
#print(codes)

inp_data = {{'100':{'id':100, 'issue': ['sth','else'], 'else': 1}},{'200':{'id':200, 'issue': ['sth','more'], 'else': 2}},{'300':{'id':300, 'issue': ['sth','mas'], 'else': 3}}}
df = pd.DataFrame(inp_data)
print(df)