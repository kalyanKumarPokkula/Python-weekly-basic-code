class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"name of a person is {self.name} age is {self.age} and gender is {self.gender}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("provide a valid age not in negative value")
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if gender not in ["male", "female", "transgender"]:
            raise ValueError("provide a valid gender not in negative value")
        self._gender = gender


def main():
    person = Person("avinash", 22, "male")
    print(person)


if __name__ == "__main__":
    main()
