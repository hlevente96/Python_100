import pandas as pd

df = pd.read_csv("day25.csv")
print(df["Primary Fur Color"].value_counts())