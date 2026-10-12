import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/deehd/OneDrive/Desktop/py/python/pandas/data.csv")

type1_count = data["Type1"].value_counts()

plt.barh(type1_count.index, type1_count.values, edgecolor = "black")
plt.tight_layout()
plt.show()