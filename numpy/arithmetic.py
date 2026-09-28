import numpy as np

array1 = np.array([23, 45, 56, 12, 78, 89, 95])
array2 = np.array([67, 73, 90, 18, 30, 82, 64])

print("=" * 10, "SCALAR ARITHMETIC", "=" * 10)
print("Addition by 23")
print(array1 + 23)
print("\n")
print(" Power of 2")
print(array1 ** 2)
print("\n")

print("=" * 10, "VECTORIZED ARITHMETIC", "=" * 10)
print("Square root")
print(np.sqrt(array1))
print("\n")
print("Area of a Circle")
print(np.pi * array1 ** 2)
print("\n")

print("=" * 10, "ELEMENT WISE ARITHMETIC", "=" * 10)
print("Addition of the two arrays")
print(array1 + array2)
print("\n")

print("=" * 10, "COMPARISON ARITHMETIC", "=" * 10)
print("Any number greatoe than 50")
print(array1 > 50)
print("\n")
print("Without using boolean, numbers less than 50 = 0")
array1[array1 < 50] = 0
print(array1)