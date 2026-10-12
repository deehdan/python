import matplotlib.pyplot as plt
import numpy as np

categories = ["Orange", "Banana", "Apple", "Watermelon", "Mango"]
count = np.array([23, 40, 15, 7, 25])

colors = ["orange", "yellow", "red", "green", "lightyellow"]

plt.pie(count, 
        labels = categories,
        autopct = "%1.1f%%",
        explode = [0, 0, 0 , 0, 0.1],
        shadow = True,
        startangle = 180,
        colors = colors)

plt.show()