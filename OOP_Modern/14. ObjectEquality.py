from collections import namedtuple


class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        """Without this the output would be
        <__main__.Book object at 0x000001B861E56F70>
        The structure should resemble the class creation syntax
        Book('Cars for beginners','Nassim','Hardcover',519)"""
        return f"Book('{self.title}','{self.author}','{self.book_type}',{self.pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False  # Equality test, lets make objects equal if titles and authors are same

        return self.title == other.title and self.author == other.author


essay = namedtuple("essay", ["title", "author"])
e = essay("Cars for beginners", "Nassim")

b1 = Book("Cars for beginners", "Nassim", "Hardcover", 519)
b2 = Book("Cars for beginners", "Nassim", "Hardcover", 519)

print(b1.__eq__(b2))
