class Student:
    setRoll = 0  # static variable

    def __init__(self, name, age):
        if not name:
            raise ValueError("missing name")
        Student.setRoll += 1
        self.rollNumber = self.setRoll
        self.name = name
        self.age = age

    def __str__(self):
        return f"student name is {self.name} and age is {self.age} and roll number is {self.rollNumber}"


def main():
    student1 = Student(input("Name :"), input("Age :"))
    print(student1)


if __name__ == "__main__":
    main()
