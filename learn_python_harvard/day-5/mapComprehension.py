students = ["Abhaya", "Nirbhaya", "Jay", "Vijay"]

# list comprehension
studentList = [{"name": student, "dept": "science"} for student in students]
print(studentList)

# map comprehension
studentMap = {student : "science" for student in students}
print(studentMap)


for i, student in enumerate(students):
    print(i+1, student) 