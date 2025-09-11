class Student:
    def __init__(self, name, stream):
        self.name = name
        """
        It will call the setter method to assign value through validation
        """
        self.stream = stream

    def __str__(self):
        return f"Student name is {self.name}, from {self.stream} class. He got {self.marks}"

    # Getter method
    @property
    def name(self):
        return self._name

    # Setter method
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("name is missing")
        """
        used '_name' as to differentiate between property name and function name
        self._name shall not invoke the setter function to assign value, 
        it is to direct assign value in the property
        """
        self._name = name

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, stream):
        if stream not in ["science", "arts", "commerce"]:
            raise ValueError("Not a valid stream")
        self._stream = stream


def getStudent():
    name = input("Enter name: ")
    stream = input("Enter stream: ")
    return Student(name, stream)


def main():
    student = getStudent()
    student.marks = "60"
    """
    It is allowed and bypass the validation
    student._stream = "wrong stream";

    Convention is that
    1. If an instance variable starts with _(underscore), pls don't touch it.
    2. If an instance variable starts with __(double underscore), pls don't touch it.
    """
    print(student)


if __name__ == "__main__":
    main()
