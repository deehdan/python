import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 11], dtype = np.int64)

array = array.astype(np.float32)

array1 = np.array(["Cate", "Dedan", "Joseph", "Lucy"], dtype = "<U4")

print(array)
print(array.dtype)
print(f"{array.nbytes} Bytes")

print("=" * 35)

print(array1)
print(array1.dtype)
print(f"{array1.nbytes} Bytes")