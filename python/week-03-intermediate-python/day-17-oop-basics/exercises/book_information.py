# Book Information
# Practices constructors, instance attributes, return values, and multiple objects.


class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_summary(self):
        return f"{self.title} by {self.author} ({self.page_count} pages)"

    def is_long_book(self):
        return self.page_count > 300


book_1 = Book("The Pragmatic Programmer", "David Thomas and Andrew Hunt", 352)
book_2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 504)

print("\n==========================================")
print("             BOOK INFORMATION             ")
print("==========================================\n")

print(book_1.get_summary())
print(f"Long book: {book_1.is_long_book()}")

print()

print(book_2.get_summary())
print(f"Long book: {book_2.is_long_book()}")
