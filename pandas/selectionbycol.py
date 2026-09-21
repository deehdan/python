import pandas as pd

read = pd.read_csv("pandas/data.csv")

#For a single column
#print(read["Height"].to_string())

#For multiple columns
print(read[["Name", "Height", "Weight"]])