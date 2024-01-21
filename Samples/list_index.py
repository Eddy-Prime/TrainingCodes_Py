
class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        


    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"ISBN: {self.isbn}")
    

def add_book_to_library(library, title, author, genre, isbn):
    book = Book(title, author, genre, isbn)
    library.append(book)

def display_library(library):
    for book in library:
        book.display_info()

# Example usage:
library = []

# Adding books to the library
add_book_to_library(library, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "978-3-16-148410-0")
add_book_to_library(library, "To Kill a Mockingbird", "Harper Lee", "Classics", "978-0-06-112008-4")
add_book_to_library(library, "1984", "George Orwell", "Dystopian", "978-0-452-28423-4")

# Displaying the library
display_library(library)
