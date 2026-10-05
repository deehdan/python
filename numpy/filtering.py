import numpy as np

age = np.array([[17, 2, 53, 78, 34],
                  [12, 45, 96, 3, 67]])

adult = age[age >= 18]
working = age[(age >= 18) & (age <= 60)]
evenage = age[age % 2 == 0]
oddage = age[age % 2 != 0]
over18 = np.where(age >= 18, age, 0 )

print(adult)
print(working)
print(evenage)
print(oddage)
print(over18)