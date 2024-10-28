from typing import List
from .book import Book

class Reader:
    def __init__(self, name: str, reader_id: int):
        self._name = name  # Managed attribute
        self.reader_id = reader_id
        self.read_books: List[Book] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Имя не может быть пустым.")
        self._name = value

    def read_book(self, book: Book):
        self.read_books.append(book)

    def __str__(self):
        return f"Reader(name={self.name}, id={self.reader_id})"

    def __eq__(self, other):
        if not isinstance(other, Reader):
            return NotImplemented
        return self.reader_id == other.reader_id

    def __len__(self):
        return len(self.read_books)

    @property
    def total_pages_read(self) -> int:
        return sum(book.pages for book in self.read_books)
