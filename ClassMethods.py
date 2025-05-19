class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create book objects
b1 = Book("Python Basics")
b2 = Book("OOP in Python")
b3 = Book("Data Structures")
b4 = Book("Algorithms")
b5 = Book("Machine Learning")

# Check total book count
print("Total books added:", Book.total_books)
