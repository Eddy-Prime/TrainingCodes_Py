class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year # This will invoke the setter

    #getter
    @property
    def year(self):
        return self._year
    
    #setter
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Year must be a positive integer!")
        self._year = value

    def get_info(self):
        return f"{self.title} by {self.author}, {self.year}"

class Library:
    def __init__(self, name: str):
        self.name = name
        self._books = [] #private field

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        if all(b.title.lower() != book.title.lower() or b.author.lower() != book.author.lower() for b in self._books):
            self._books.append(book)

    def remove_book(self, title, author):
        titleLower = title.lower()
        authorLower = author.lower()
        self._books = [b for b in self._books if not (b.title.lower() == titleLower and b.author.lower() == authorLower)]
