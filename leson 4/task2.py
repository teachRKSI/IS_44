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


s = Student("Борис", 17)

print(Student.is_adult(20))
print(s.is_adult(20))

student = Student.from_string("Аня,20")

print(student.name)
print(student.age)