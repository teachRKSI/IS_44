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


if __name__ == "__main__":
    s = Student("Борис", 19)

    print("Вызов через класс:", Student.is_adult(20))
    print("Вызов через экземпляр:", s.is_adult(16))

    student = Student.from_string("Аня,20")
    print(f"Студент создан из строки: {student.name}, возраст: {student.age}, вуз: {student.university}")
