class Book:
def __init__(self, title, author, year, is_read=False):
self.title = title
self.author = author
self.year = year
self.is_read = is_read

def mark_as_read(self):
self.is_read = True

def __str__(self):
status = "прочитана" if self.is_read else "не прочитана"
return f"«{self.title}» — {self.author}, {self.year} г. ({status})"

def __repr__(self):
return f"Book({self.title!r}, {self.author!r}, {self.year!r}, {self.is_read!r})"


class Library:
def __init__(self):
self.books = []

def add(self, book):
self.books.append(book)

def find_by_author(self, author):
return [book for book in self.books if book.author == author]

def unread(self):
return [book for book in self.books if not book.is_read]

def __len__(self):
return len(self.books)

def __str__(self):
return f"Библиотека содержит {len(self.books)} книг"


class DigitalLibrary(Library):
def __init__(self, format):
super().__init__()
self.format = format

def __str__(self):
return super().__str__() + f". Формат: {self.format}"


# Создание книг
book1 = Book("Война и мир", "Толстой", 1869)
book2 = Book("Преступление и наказание", "Достоевский", 1866)
book3 = Book("Анна Каренина", "Толстой", 1877)

# Создание библиотеки
library = Library()

library.add(book1)
library.add(book2)
library.add(book3)

# Отмечаем книгу как прочитанную
book1.mark_as_read()

print("Все книги:")
for book in library.books:
print(book)

print("\nКниги Толстого:")
for book in library.find_by_author("Толстой"):
print(book)

print("\nНепрочитанные книги:")
for book in library.unread():
print(book)

print("\nКоличество книг:", len(library))

# Создание цифровой библиотеки
digital = DigitalLibrary("pdf")
digital.add(Book("Python", "Марк Лутц", 2013))

print("\n", digital)