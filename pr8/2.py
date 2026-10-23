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

anya = Student("Аня", 20)
print(Student.is_adult(20))
print(anya.is_adult(20))
print(Student.from_string("Аня,20"))
print(Student.from_string("Аня,20").age)
print(Student.from_string("Аня,20").name)


