

class Book:

    def __init__(self, id, name, price, pages, author, type):
        self.id = id
        self.name = name
        self.price = price
        self.pages = pages
        self.author = author
        self.type = type

    def book_detail(self):
        book_detail = (self.id, self.name, self.price, self.pages, self.author, self.type)
        return book_detail

class Magazine(Book):
    def __init__(self, id, name, price, pages, author,  type, month, creator):
        Book.__init__(self, id, name, price, pages, author, type)

        self.month = month
        self.creator = creator

    def magazine_detail(self):
        book_detail = (self.id, self.name, self.price, self.pages, self.author,  self.type, self.month, self.creator)
        return book_detail


class Novel(Book):
    def __init__(self, id, name, price, pages, author, type, writer):
        Book.__init__(self, id, name, price, pages, author, type)

        self.writer = writer

    def novel_detail(self):
        book_detail = (self.id, self.name, self.price, self.pages, self.author, self.type, self.writer)
        return book_detail

