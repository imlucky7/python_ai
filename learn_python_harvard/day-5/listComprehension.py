list1 = ["this", "is", "list"]
students = [
    {"name": "Navin", "sub": "science"},
    {"name": "Pravin", "sub": "arts"},
    {"name": "Nutan", "sub": "science"},
    {"name": "Puran", "sub": "commerce"},
]


def main():
    # List comprehension
    uppercased = [l1.upper() for l1 in list1]
    print(*uppercased)

    # List comprehension
    studentList = [student["name"] for student in students if student["sub"] == "science"]
    for stud in sorted(studentList):
        print(stud)

    # Filter
    studentMaptFil = filter(lambda s: s["sub"] == "science", students)

    for studMap in sorted(studentMaptFil, key=lambda s: s["name"]):
        print(studMap["name"])


if __name__ == "__main__":
    main()
