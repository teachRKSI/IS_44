#Задание 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed       # забыли super()

    def info(self):
        return f"{self.name}, порода: {self.breed}"

    def speak(self):
        return(f'{super().speak()} (гав!)')

d = Dog('Собака', 'Лабрадор')
print(d.info())
print(d.speak())

#Задание 2
class Student:
    university = "МГУ"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod 
    def is_adult(age):
        if age >= 18:
            return True

    @classmethod
    def from_string(cls, s):
        name, age = s.split(',')
        return cls(name, age)

s = Student('Оноколов А.А.', 19)
print(s.is_adult(20))
print(Student.is_adult(20))

s2 = Student.from_string('Аня,20')
print(s2.name, s2.age)

#Задание 3
class Library:
    def __init__(self, lib=None):
        self.lib = lib if lib is not None else []

    def add(self, book):
        self.lib.append(book)

    def find_by_author(self, author):
        finding_result = [book for book in self.lib if book.author == author]
        return finding_result

    def unread(self):
        unread_books = [book for book in self.lib if not book.is_read]
        return unread_books

    def __len__(self):
        return len(self.lib)

    def __str__(self):
        assort = []
        for book in self.lib:
            assort.append(str(book)) 
        result = '\n\n'.join(assort)
        return f'-=Ассортимент библиотеки=-\n{result}'

class Book:
    def __init__(self, title, author, year, is_read=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def __str__(self):
        return f'-=Описание книги=-\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nПрочитана: {self.is_read}'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.is_read})"

class DigitalLibrary(Library):
    def __init__(self, format):
        super().__init__()
        self.format = format

    def __str__(self):
        return f'{super().__str__()}\nФормат: {self.format}'

    


book1 = Book('Муму', 'И.С.Тургенев', 2020)
book2 = Book('Обломов', 'И.А.Гончаров', 2023, True)
book3 = Book('Война и мир', 'Л.Н.Толстой', 2001)
lib1 = Library([book1, book2])
lib1.add(book3)
print(lib1.find_by_author('И.А.Гончаров'))
print(lib1.unread())
print(len(lib1))
print(str(lib1))
digital1 = DigitalLibrary('pdf')
digital1.add(book1)
print(str(digital1))