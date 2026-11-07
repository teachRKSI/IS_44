class Student:
    university = "МГУ"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))


# Проверка 1: staticmethod
print(Student.is_adult(20))  # True
s = Student("Аня", 17)
print(s.is_adult(20))        # True

# Проверка 2: classmethod
s2 = Student.from_string("Аня,20")
print(s2.name, s2.age)       # Аня 20
print(type(s2))              # <class '__main__.Student'>