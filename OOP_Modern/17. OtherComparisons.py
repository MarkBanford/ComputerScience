'''ie b1>b2 is not defined yet'''


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

    def __hash__(self):
        return hash((self.title, self.author))

    def __gt__(self, other):  # greater than
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages <= other.pages

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages >= other.pages


b1 = Book("Cars for beginners", "Nassim", "Hardcover", 520)
b2 = Book("Cars for beginners", "Nassim", "Hardcover", 519)

print(b1 >= b2)
