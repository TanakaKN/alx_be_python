# Book class to hold book information
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __repr__(self):
        return f"{self.title} by {self.author}"


# Library class to manage the books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"You checked out: {book}")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                print(f"You returned: {book}")
                return
        print("This book was not checked out")

    def list_available_books(self):
        print("Available books:")
        for book in self.books:
            if not book.is_checked_out:
                print(book)
