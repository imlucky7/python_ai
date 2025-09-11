import random


class Student:
    streams = ["Science", "Commerce", "Arts"]
    deptPassMarksPer = {"Science": 75, "Commerce": 80, "Arts": 65}

    @classmethod
    def sort(cls, name):
        print(f"{name} is enroled in", random.choice(cls.streams))

    @staticmethod
    def isPromoted(dept, marks):
        passMarks = Student.deptPassMarksPer.get(dept)
        if marks >= passMarks:
            print("Promoted")
        else:
            print("Not Promoted")


def main():
    Student.sort("asd")
    Student.isPromoted("Science", 66)


if __name__ == "__main__":
    main()
