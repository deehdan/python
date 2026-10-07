import matplotlib.pyplot as plt
import numpy as np

year = np.array([2004, 2005, 2006, 2007, 2008, 2009])
class4 = np.array([34, 45, 39, 50, 51, 47])


line_style = {"marker": "*",
              "markersize" : 5,
              "markerfacecolor" : "cyan",
              "markeredgecolor" : "black",
              "linestyle" : "solid",
              "linewidth" : 1,
              }
font_style = {"fontsize" : 20,
              "family" : "Arial",
              "color" : "#2d4cfc"}

plt.plot(year, class4, color = "green", **line_style)
plt.title("No of Students by Years", 
           fontweight = "bold",
           **font_style
          )

plt.xlabel("Year", **font_style)
plt.ylabel("No of Students", **font_style)

plt.xticks(year)
plt.tick_params(axis= "both",
                color = "green")
plt.subplots_adjust(bottom= 0.175,
                    left= 0.2)

plt.grid(axis = "both",
         linewidth = 1,
         color = "lightgray")

plt.show()