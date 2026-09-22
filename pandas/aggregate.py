import pandas as pd

data = pd.read_csv("pandas/data.csv")

#whole dataframe
#print(data.mean(numeric_only=True))
#print(data.min(numeric_only=True))
#print(data.max(numeric_only=True))
#print(data.sum(numeric_only=True))
#print(data.count())

#single column
#print(data["Height"].mean())
#print(data["Height"].min())
#print(data["Height"].max())
#print(data["Height"].sum())
#print(data["Height"].count())

#Using groupby()
#group = data.groupby("Type1")
#print(group["Height"].mean())

group = data.groupby("Type1")
print(group["Height"].count())