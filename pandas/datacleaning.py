import pandas as pd

data = pd.read_csv("pandas/data.csv")

#1. Drop irrelevant columns
#data = data.drop(columns=["Legendary"])

#2. Handle missing data
#data = data.dropna(subset=["Type2"])
#data = data.fillna({"Type2" : "None"})

#3. Fix inconsistent values
#data["Type1"] = data["Type1"].replace({"Grass" : "GRASS"})

#4. Standardize text
data["Name"] = data["Name"].str.upper()

#5. Fix data types
data["Legendary"] = data["Legendary"].astype(bool)

#6. Drop duplicates
data = data.drop_duplicates()

print(data.to_string())