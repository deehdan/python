import matplotlib.pyplot as plt
import numpy as np

x = np.array([2004, 2005, 2006, 2007, 2008, 2009])
y = np.array([34, 45, 39, 50, 51, 47])
y1 = np.array([45, 43, 40, 47, 54, 45])

line_style = {"marker": "*",
              "markersize" : 5,
              "markerfacecolor" : "cyan",
              "markeredgecolor" : "black",
              "linestyle" : "solid",
              "linewidth" : 1,
              }

plt.plot(x, y, color = "green", **line_style)
plt.plot(x, y1, color = "blue", **line_style)

plt.show()