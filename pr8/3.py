class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def __str__(self):
        return f'{self.title} - {self.author}. Год: {self.year}. {"Прочитана" if self.is_read else "Не прочитана"}'

    def __repr__(self):
        return f'{self.title} {self.author} {self.year} {self.is_read}'


class Library:
    def __init__(self, library):
        self.library = library
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        for book in self.books:
            if book.author == author:
                return book

    def unread(self):
        unread = []
        for book in self.books:
            if book.is_read == False:
                unread.append(book)
        return unread

    def len(self):
        return len(self.books)

class DigitalLibrary(Library):
    def __init__(self, title, author, year, is_read, format):
        super().__init__(title, author, year, is_read)
        self.format = f'{super().str()}, {format}'
