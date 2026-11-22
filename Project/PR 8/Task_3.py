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
        return f"«{self.title}» — {self.author} ({self.year} г.) [{status}]"

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"year={self.year!r}, is_read={self.is_read!r})"
        )


class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def unread(self):
        return [book for book in self._books if not book.is_read]

    def __len__(self):
        return len(self._books)

    def __str__(self):
        return f"Библиотека (книг: {len(self)})"


class DigitalLibrary(Library):
    def __init__(self, file_format):
        super().__init__()
        self.format = file_format

    def __str__(self):
        return f"{super().__str__()}, формат: {self.format}"


b1 = Book("Война и мир", "Л. Н. Толстой", 1869)
b2 = Book("Преступление и наказание", "Ф. М. Достоевский", 1866)
b3 = Book("Анна Каренина", "Л. Н. Толстой", 1877)

b1.mark_as_read()
print(b1)
print(repr(b2))

lib = DigitalLibrary("epub")
lib.add(b1)
lib.add(b2)
lib.add(b3)

print(lib)
print("Всего книг:", len(lib))
print("Книги Толстого:", lib.find_by_author("Л. Н. Толстой"))
print("Непрочитанные:", lib.unread())