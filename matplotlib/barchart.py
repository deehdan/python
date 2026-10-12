import matplotlib.pyplot as plt
import numpy as np

categories = ["Orange", "Banana", "Apple", "Watermelon", "Mango"]
count = np.array([23, 40, 15, 7, 25])

plt.bar(categories, count, edgecolor = "black")
# plt.barh(categories, count, edgecolor = "black")  for horizontal bar chart 
plt.tight_layout()

plt.show()