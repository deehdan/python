import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc = 80, scale = 10, size = 50)

plt.hist(scores, 
         bins = 10,
         edgecolor = "black")
plt.show()