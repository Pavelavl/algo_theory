from typing import List
from .book import Book

class Reader:
    def __init__(self, name: str, reader_id: int):
        self.name = name
        self.reader_id = reader_id
        self.read_books: List[Book] = []

    def read_book(self, book: Book):
        self.read_books.append(book)

    def __str__(self):
        return f"Reader(name={self.name}, id={self.reader_id})"

    def __eq__(self, other):
        return self.reader_id == other.reader_id

    @property
    def total_pages_read(self) -> int:
        return sum(book.pages for book in self.read_books)
