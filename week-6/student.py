from person import Person


class Student(Person):
    Id = 1000

    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        Student.Id += 1
        self.studentId = Student.Id
        self.grade = grade

    def __str__(self):
        return f"student id is {self.studentId} name is {super().name} age is {super().age} and gender is {super().gender} student studing in grade {self.grade}"
