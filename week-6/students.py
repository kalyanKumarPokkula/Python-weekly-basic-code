class Student:
    setRoll = 0  # static variable

    def __init__(self, name, age):
        Student.setRoll += 1
        self.rollNumber = self.setRoll
        self.name = name
        self.age = age

    def __str__(self):
        return f"student name is {self.name} and age is {self.age} and roll number is {self.rollNumber}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing value")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("enter proper age")
        self._age = age


def main():
    student = Student(input("Name :"), int(input("Age :")))
    print(student)


if __name__ == "__main__":
    main()
