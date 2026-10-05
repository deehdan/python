import numpy as np

# randomN = np.random.default_rng() # rng(seed = 1) -- keeps the same result

# print(randomN.integers(low = 0, high = 100, size = (3, 2)))

# print(np.random.uniform(low = 0, high = 1, size = (3, 2) )) # for floats

# SHUFFLE
# rng = np.random.default_rng()
# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)
# print(array)

#Random Choice
rng = np.random.default_rng()
names = np.array(["Cate", "Kelly", "Dedan", "Jose", "John", "Mike", "Tom"])
# name = rng.choice(names)
name = rng.choice(names, size = (2, 3, 2))
print(name)
