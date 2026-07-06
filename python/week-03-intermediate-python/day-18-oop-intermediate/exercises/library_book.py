# Library Book
# Tracks availability and prevents invalid borrow or return actions.


class LibraryBook:
    def __init__(self, title, author):
        self.title = " ".join(title.split()).title()
        self.author = " ".join(author.split()).title()
        
        self.book_id = f"{self.title[:3]}-{self.author[:3]}".replace(" ", "").lower()
        
        self.is_available = True

    def borrow_book(self):
        if not self.is_available:
            return False
        
        self.is_available = False
        return True

    def return_book(self):
        if self.is_available:
            return False

        self.is_available = True
        return True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id} | {self.title} by {self.author} | {status}"


print("\n==========================================")
print("               LIBRARY BOOK               ")
print("==========================================\n")

book = LibraryBook(
    "automate the boring stuff with python",
    "al sweigart",
)

print(f"First borrow succeeded: {book.borrow_book()}")
print(f"Second borrow succeeded: {book.borrow_book()}")
print(book)

print()

print(f"First return succeeded: {book.return_book()}")
print(f"Second return succeeded: {book.return_book()}")
print(book)


    