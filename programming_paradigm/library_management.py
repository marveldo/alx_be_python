class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
       
    def is_checked_out(self):
        return self._is_checked_out
    def set_is_checked_out(self, value : bool):
        if type(value) != bool :
            raise ValueError('Value must be bool')
        else : 
            self._is_checked_out = value

class Library:

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self,title) :
        for book in self._books:
            if book.title == title and not book.is_checked_out() :
                book.set_is_checked_out(True)
    def return_book(self,title) :
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.set_is_checked_out(False)
    def list_available_books(self):
        available_books = [book for book in self._books]
        for book in available_books :
            if not book.is_checked_out():
               print(f"{book.title} {book.author}")
    