# Exam Task: Class Book and Class Library

## Class Book

The class `Book` represents books in a library. Each book has a title, author, and year of publication.

### Define a class `Book`.

#### Define Book's constructor:
- The constructor takes three parameters: `title` (a string), `author` (a string), and `year` (an integer).
- Store `title` and `author` in public fields.
- Store `year` in a private field, accessible via a property.
- Define a setter for `year`.
  - The year must be a positive integer. If a non-positive integer is provided, the setter should raise a `ValueError`.

#### Define a method `get_info()` which returns a string representation of the book in the format "Title by Author, Year".

### Example:

## Class Library

The class `Library` represents a collection of books.

### Define a class `Library`.

#### Define Library's constructor:
- The constructor takes one parameter: `name` (a string).
- A `Library` also includes a field `books` which is a list of `Book` objects. This list is empty when a `Library` is created.
- Store `name` in a public field.
- Store `books` in a private field accessible via a property.

#### Define a method `add_book(book)` which adds a `Book` to `books`.
- A `Book` should not be added if a `Book` with the same title and author is already present in the list. While checking for duplicates, ignore case differences.

#### Define a method `remove_book(title, author)` which removes a `Book` from `books`, based on the title and author provided.
- If this book is not in `books`, do nothing. Ignore case differences while checking for the book.

Both `add_book(book)` and `remove_book(title, author)` possibly change the value of the field `books` but do not return anything.


