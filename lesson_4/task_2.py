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


s = Student.from_string("Аня,20")
print("Студент:", s.name, s.age)
print("Через класс:", Student.is_adult(20))
print("Через объект:", s.is_adult(20))
print("В 17 лет:", Student.is_adult(17))
