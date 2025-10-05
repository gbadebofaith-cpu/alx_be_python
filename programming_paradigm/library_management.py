class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class that manages a collection of books."""

    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"'{book.title}' has been checked out.")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Return a book by title if it exists in the library."""
        for book in self._books:
            if book.title.lower() == title.lower():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
