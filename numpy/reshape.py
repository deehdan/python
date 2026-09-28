import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

numbers = numbers.reshape(4, 3)

print(numbers)

print("=" * 20)

digits = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

digits = digits.reshape(3, 2, 2)

print(digits)

print("=" * 20)

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

nums = nums.reshape(1, -1)

print(nums)