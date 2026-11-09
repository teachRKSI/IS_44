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

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age})"

print(Student.is_adult(20))
s = Student("Аня", 17)
print(s.is_adult(20))
print(s.is_adult(s.age))

s2 = Student.from_string("Борис,22")
print(s2)
print(type(s2))
print(s2.university)