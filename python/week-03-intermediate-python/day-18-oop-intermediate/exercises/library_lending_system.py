# Library Lending System
# Combines two simple record classes without using inheritance.


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = " ".join(name.split()).title()
        self.member_id = member_id.strip().upper()
        self.borrowed_book = None

    def can_borrow(self):
        return self.borrowed_book is None

    def borrow_book(self, book):
        if not self.can_borrow() or not book.is_available:
            return False

        if book.borrow(self.member_id):
            self.borrowed_book = book
            return True

        return False

    def return_book(self):
        if self.borrowed_book is None:
            return False

        book_to_return = self.borrowed_book

        if book_to_return.return_book(self.member_id):
            self.borrowed_book = None
            return True

        return False

    def __str__(self):
        if self.borrowed_book is None:
            borrowed_title = "None"
        else:
            borrowed_title = self.borrowed_book.title

        return (
            f"{self.member_id} | {self.name} | "
            f"Borrowed book: {borrowed_title}"
        )


class LibraryBook:
    def __init__(self, title, author, book_id):
        self.title = " ".join(title.split()).title()
        self.author = " ".join(author.split()).title()
        self.book_id = book_id.strip().upper()
        self.is_available = True
        self.borrowed_by = None

    def borrow(self, member_id):
        if not self.is_available:
            return False

        self.is_available = False
        self.borrowed_by = member_id
        return True

    def return_book(self, member_id):
        if self.is_available or self.borrowed_by != member_id:
            return False

        self.is_available = True
        self.borrowed_by = None
        return True

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = f"Borrowed by {self.borrowed_by}"

        return f"{self.book_id} | {self.title} by {self.author} | {status}"


print("\n==============================================")
print("          LIBRARY LENDING SYSTEM              ")
print("==============================================\n")

python_book = LibraryBook(
    "automate the boring stuff with python",
    "al sweigart",
    "py-101",
)
clean_code_book = LibraryBook("clean code", "robert c. martin", "se-201")

kashif = LibraryMember("kashif rezwi", "mem-001")
meera = LibraryMember("meera sharma", "mem-002")

print("--- Initial Records ---")
print(python_book)
print(clean_code_book)
print(kashif)
print(meera)

print("\n--- Lending Actions ---")

if kashif.borrow_book(python_book):
    print(f"{kashif.name} borrowed {python_book.title}.")
else:
    print("Borrow request failed.")

if meera.borrow_book(python_book):
    print(f"{meera.name} borrowed {python_book.title}.")
else:
    print(f"{python_book.title} is not available for {meera.name}.")

if meera.borrow_book(clean_code_book):
    print(f"{meera.name} borrowed {clean_code_book.title}.")
else:
    print("Borrow request failed.")

print("\n--- Records After Borrowing ---")
print(python_book)
print(clean_code_book)
print(kashif)
print(meera)

print("\n--- Return Action ---")

if kashif.return_book():
    print(f"{kashif.name} returned the book.")
else:
    print("Return request failed.")

print("\n--- Final Records ---")
print(python_book)
print(clean_code_book)
print(kashif)
print(meera)
