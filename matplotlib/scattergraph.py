import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 3, 4, 5, 6])
y = np.array([23, 24, 25, 26, 28])

x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([20, 21 , 23, 27, 28])

plt.scatter(x, 
            y,
            color = "blue",
            label = "class A")

plt.scatter(x1, 
            y1,
            color = "red",
            label = "class B")

plt.legend()
plt.show()