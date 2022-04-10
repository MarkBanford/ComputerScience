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

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.author}"
        return repr(self)


b = Book("Cars for beginners", "Nassim", "Hardcover", 519)

print(eval(repr(b)))

print(f"{b:short}")
