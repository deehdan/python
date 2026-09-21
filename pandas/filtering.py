import pandas as pd

data = pd.read_csv("pandas/data.csv")

#print height >= 2 
#tall = data[data["Height"] >= 2]
#print(tall)

#print those with type1 or type2 as water
#water = data[(data["Type1"] == "Water") | (data["Type2"] == "Water")]
#print(water)

#print those with fire as type1 and flying as type2
ff = data[(data["Type1"] == "Fire") & (data["Type2"] == "Flying")]
print(ff)