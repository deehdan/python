import pandas as pd

data = pd.read_csv("pandas/data.csv")

# print(data) => only prints the first and last 5

print(data.to_string())