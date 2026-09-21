import pandas as pd

students = {"Cate" : 98, "Dan" : 97, "Jos" : 95}

series = pd.Series(students)

print(series)

series.loc["Jos"] += 1

print("Updated list \n", series)