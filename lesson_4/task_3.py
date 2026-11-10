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
        return f"{self.title} - {self.author} ({self.year} г., {status})"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year}, is_read={self.is_read})"


class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def unread(self):
        return [b for b in self.books if not b.is_read]

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Библиотека (книг: {len(self.books)})"


class DigitalLibrary(Library):
    def __init__(self, format):
        super().__init__()
        self.format = format

    def __str__(self):
        return f"{super().__str__()}, формат: {self.format}"


if __name__ == "__main__":
    b1 = Book("Война и мир", "Л. Толстой", 1869)
    b2 = Book("Анна Каренина", "Л. Толстой", 1877)
    b3 = Book("Преступление и наказание", "Ф. Достоевский", 1866)

    b1.mark_as_read()

    print("Книги:")
    print(b1)
    print(b2)

    lib = Library()
    lib.add(b1)
    lib.add(b2)
    lib.add(b3)

    print("\nОбычная библиотека:")
    print(lib)
    print("Всего книг:", len(lib))
    print("Книги Толстого:", lib.find_by_author("Л. Толстой"))
    print("Непрочитанные книги:", lib.unread())

    dig_lib = DigitalLibrary("pdf")
    dig_lib.add(b1)
    dig_lib.add(b2)

    print("\nЭлектронная библиотека:")
    print(dig_lib)
    print("Всего книг в электронной библиотеке:", len(dig_lib))
