'''Build a container class for our books, a book-shelf as a way to interact with them'''


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
b2 = Book("The circle", "Dave", "Paperback", 497)
b3 = Book("Titan", "Ron", "Hardcover", 830)


class BookShelf:
    def __init__(self, capacity):
        self.books = []  # every bookshelf will have its own list of books
        self.capacity = capacity

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only instances of Book can be added")
        if not self.capacity > len(self.books):
            raise OverflowError("Bookshelf is full")
        self.books.append(book)

    def __repr__(self):
        return str(self.books)

    def __add__(self, other):
        self.books.append(other)
        return self.books


shelf = BookShelf(10)
shelf.add_book(b1)
shelf.add_book(b2)
print(shelf)
shelf+b3
print(shelf)