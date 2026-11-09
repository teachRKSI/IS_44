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
        return f"«{self.title}», {self.author}, {self.year} г. — {status}"

    def __repr__(self):
        return (f"Book({self.title!r}, {self.author!r}, "
                f"{self.year}, is_read={self.is_read})")


class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        return result

    def unread(self):
        result = []
        for book in self.books:
            if not book.is_read:
                result.append(book)
        return result

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Библиотека: {len(self)} книг"


class DigitalLibrary(Library):
    def __init__(self, format):
        super().__init__()
        self.format = format

    def __str__(self):
        return f"{super().__str__()}, формат: {self.format}"


book1 = Book("Капитанская дочка", "Пушкин", 1836)
book2 = Book("Дубровский", "Пушкин", 1841)
book3 = Book("Ревизор", "Гоголь", 1836)
book1.mark_as_read()

library = DigitalLibrary("pdf")
library.add(book1)
library.add(book2)
library.add(book3)

print(library)
print("Количество книг:", len(library))
print("Для отладки:", repr(book1))

print("Книги Пушкина:")
for book in library.find_by_author("Пушкин"):
    print(book)

print("Непрочитанные книги:")
for book in library.unread():
    print(book)
