import pandas as pd

results = []

def result(name , marks , grade):
    details = {
        "name" : name,
        "marks" : marks,
        "grade" : grade
    }
    return details

while True:
    name = input("Enter your name: ")
    print("Enter you marks below")

    while True:
        maths = int(input("Maths: "))
        coding = int(input("Coding: "))
        physics = int(input("Physics: "))

        student_marks = 0

        if maths < 0 or maths >100 or coding < 0 or coding >100 or physics < 0 or physics >100:
            print("Invalid")
        else: 
            student_marks = (maths + coding + physics) / 3
            print(student_marks)
            break

    if student_marks > 90: 
        grade = "Grade A"
    elif student_marks > 59:
        grade = "Grade B"
    elif student_marks > 49: 
        grade = "Grade C"
    else: 
        grade = "Work hard."

    print(grade)

    #create new student
    new_student = result(name, student_marks, grade)

    #add a student
    results.append(new_student)
    print("Student added succeessfully!")

    cont = input("Do you want to enter another student? (y/n): ")
    if cont != "y":
        print("Bye")
        break

classdata = pd.DataFrame(results)
classdata = classdata.sort_values(by = "marks", ascending = False)
print(classdata)

# create a csv file
#classdata.to_csv("classdata.csv")