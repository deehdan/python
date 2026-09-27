import numpy as np

array = np.array([
                [["A", "B", "C"], ["D", "E", "F"],["G", "H", "J"]],
                [["K", "L", "M"], ["N", "O", "P"],["Q", "R", "S"]],
                [["T", "I", "U"], ["V", "W", "X"],["Y", "Z", "_"]]
                ])

print(array.ndim)
print(array.shape)
#print(array[0][0][0]) instead write:
print(array[0, 0, 0])

word = array[0, 0, 2] + array[0, 0, 0] + array[2, 0, 0] + array[0, 1, 1]
print(word)