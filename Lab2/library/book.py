class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self._pages = pages  # Managed attribute

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if value < 0:
            raise ValueError("Количество страниц не может быть отрицательным.")
        self._pages = value

    def get_page_count(self) -> int:
        return self.pages

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author
