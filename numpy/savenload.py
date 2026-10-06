import numpy as np

# array = np.array([1, 2, 3, 4, 5])

# np.save("data", array) -- for  one dimensional
# np.load("data.npy")

array1 = np.array([[1, 2, 33, 67],
                  [34, 5, 6, 12]])
array2 = np.array([[7, 42, 23, 97],
                  [4, 51, 56, 10]])

# np.savez("data", array1, array2)
# np.savez_compressed("data", array1, array2)

load = np.load("data.npz")
array1 = load("arr_0")