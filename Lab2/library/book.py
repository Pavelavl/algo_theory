class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def get_page_count(self) -> int:
        return self.pages

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"

    def __lt__(self, other):
        return self.pages < other.pages
