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


b1 = Book("Cars for beginners", "Nassim", "Hardcover", 519)
print(hash(b1))
b2 = Book("Cars for beginners1", "Nassim1", "Hardcover1", 519)
print(hash(b2))
b3 = Book("Cars for beginners", "Nassim", "Hardcover", 519)
print(hash(b3))
print(hash(b3) == hash(b1))
