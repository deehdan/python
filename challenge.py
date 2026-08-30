# This is a constant value
UNIVERSITY = "DeKUT"  

students = []

# This is a funtion
def student(name, age, course, favlang ):
    details = {
        "name" : name,
        "age" : age,
        "university" : UNIVERSITY,
        "course" : course,
        "favlang" : favlang
    }
    return details

while True:
    print("=" *34)
    print("Add Student")
    print("=" *34)
    name1 = input("Enter your name: ")
    age1 = input("Enter your age: ")
    course1 = input("Enter your course: ")
    favlang1 = input("Enter your favorite programming language: ")

    # Create student 
    new_student = student(name1, age1, course1, favlang1)

    #Add student to the list
    students.append(new_student)

    print("\n Student added successfully")

    #Ask if to close or keep adding student
    ans = input("Do you want to add another student? y/n: ")
    if ans == "n":
        break


print("\n" + "=" * 35)
print(" STUDENT PROFILE")
print("=" * 35)

for i, student_info in enumerate(students, start=1):
    print(f"Name : {student_info['name']}")
    print(f"Age : {student_info['age']}")
    print(f"University : {student_info['university']}")
    print(f"Course : {student_info['course']}")
    print(f"Favorite Language : {student_info['favlang']}")
    print("=" * 35)

print(f"Total Students: {len(students)}")
print("=" * 35)