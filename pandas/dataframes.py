import pandas as pd

students = {
    "Name" : ["Johnson", "James", "Peter"],
    "Age" : [21, 20, 22]
}

codingclass = pd.DataFrame(students, index = ["Student 1", "Student 2", "Student 3"])

#Adding a new column
codingclass["Grade"] = ["B", "A", "C"]

#Adding a new row
new_row = pd.DataFrame([{"Name" : "Joseph", "Age" : 19, "Grade" : "A"}], index = ["Student 4"])
codingclass = pd.concat([codingclass, new_row])

print(codingclass)