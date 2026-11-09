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
        return f"«{self.title}» — {self.author} ({self.year}), {status}"

    def __repr__(self):
        return (f"Book(title={self.title!r}, author={self.author!r}, "
                f"year={self.year}, is_read={self.is_read})")


class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def find_by_author(self, author):
        return [b for b in self._books if b.author == author]

    def unread(self):
        return [b for b in self._books if not b.is_read]

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __str__(self):
        return f"Библиотека: {len(self._books)} книг(и)"


class DigitalLibrary(Library):
    def __init__(self, format):
        super().__init__()
        self.format = format

    def __str__(self):
        return f"{super().__str__()}, формат: {self.format}"

b1 = Book("Преступление и наказание", "Достоевский", 1866)
b2 = Book("Анна Каренина", "Толстой", 1877)
b3 = Book("Мёртвые души", "Гоголь", 1842)

print(b1)
b1.mark_as_read()
print(b1)
print(repr(b2))

lib = Library()
lib.add(b1)
lib.add(b2)
lib.add(b3)

print(len(lib))
print(lib.find_by_author("Толстой"))
print(lib.unread())

for book in lib:
    print(book)

dl = DigitalLibrary("pdf")
dl.add(b1)
dl.add(b3)
print(dl)
print(len(dl))
print(dl.unread())

print(isinstance(dl, Library))
print(issubclass(DigitalLibrary, Library))