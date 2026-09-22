import pandas as pd

students = pd.read_csv("pandas/project/student.csv")

#Add average colum
students["Average"] = students[["Math", "Python", "Networking"]].mean(axis = 1)

print(students)

print("==============================")

#Find highest and lowest student
highest_student = students.loc[students["Average"].idxmax()]
print(f" THE HIGHEST STUDENT IS : \n{highest_student}")

print("==============================")

lowest_student = students.loc[students["Average"].idxmin()]
print(f" THE LOWEST STUDENT IS : \n{lowest_student}")

print("==============================")

#Count students with an average => 50
passed_students = students[students["Average"] >= 50]
print("THE PASSED STUDENTS ARE: ")
print(passed_students[["Name", "Average"]])

print("==============================")

#create a result column pass >= 50, fail < 50
students["Result"] = students["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print(students)   

print("==============================")
#Highest mark in every subject
print("HIGHEST MARK IN MATH IS: ", students["Math"].max())
print("HIGHEST MARK IN PYTHON IS: ", students["Python"].max())
print("HIGHEST MARK IN NETWORKING IS: ", students["Networking"].max())