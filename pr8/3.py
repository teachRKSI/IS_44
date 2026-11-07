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
        return f"«{self.title}» — {self.author} ({self.year} г.), {status}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year}, is_read={self.is_read})"


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

    def __str__(self):
        return f"Библиотека, книг: {len(self)}"


class DigitalLibrary(Library):
    def __init__(self, format):
        super().__init__()
        self.format = format

    def __str__(self):
        # Переопределяем __str__, вызывая родительский и дописывая формат
        return f"{super().__str__()}, формат: {self.format}"


# --- Проверка ---
b1 = Book("Война и мир", "Толстой", 1869)
b2 = Book("Анна Каренина", "Толстой", 1877)
b3 = Book("Мастер и Маргарита", "Булгаков", 1967)

lib = Library()
lib.add(b1)
lib.add(b2)
lib.add(b3)

print(len(lib))                        # 3
print(lib.find_by_author("Толстой"))   # [Book(...), Book(...)]
print(lib.unread())                    # все 3 книги (никто не читал)

b1.mark_as_read()
print(len(lib.unread()))               # 2

# Проверка DigitalLibrary
dlib = DigitalLibrary("pdf")
dlib.add(Book("Собачье сердце", "Булгаков", 1925))
print(dlib)   # Библиотека, книг: 1, формат: pdf