import pandas as pd

data = pd.read_csv("pandas/data.csv", index_col="Name")

#search by name
#print(data.loc["Moltres"])

#search and give certain rows
#print(data.loc["Ivysaur":"Charmeleon", ["Type1", "Type2"]])

#search index 0 to 10, give every second row and give only the first 3 columns
#print(data.iloc[0:11:2, 0:3])

#make the user search 
pokemon = input("Enter a Pokemon name: ")

try:
    print(data.loc[pokemon])

except:
    print(f"{pokemon} not found!")    