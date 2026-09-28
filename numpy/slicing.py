import numpy as np

nums = np.array([
                [1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12],
                [13, 14, 15, 16]
                ])

#array[start: end: step]
#ROWS
#specific row
print("=" * 10, "SPECIFIC ROW", "=" * 10)

print(nums[2])

print("=" * 10, "START TO END", "=" * 10)

#start to end
print(nums[: 2])

print("=" * 10, "STEPS", "=" * 10)

#step
print(nums[::2])

print("=" * 10, "REVERSE ROWS", "=" * 10)

#reverse rows
print(nums[: : -1])

print("=" * 10, "SPECIFIC COLUMN", "=" * 10)

#COLUMNS
#specific column
print(nums[:, 0])

print("=" * 10, "ALL 1ST 3 COLUMNS", "=" * 10)

#all first 3 columns
print(nums[:, 0: 3])

print("=" * 10, "ALL 2ND COLUMN", "=" * 10)

#all 2nd column
print(nums[:, : : 2])

print("=" * 10, "REVERSE COLUMNS", "=" * 10)

print(nums[:, : : -1])

print("=" * 10, "SPECIFIC ROWS AND COLUMNS", "=" * 10)

print(nums[2:, 2:3 ])