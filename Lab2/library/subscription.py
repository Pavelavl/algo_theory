from abc import ABC, abstractmethod
from .reader import Reader

class Subscription(ABC):
    def __init__(self, reader: Reader, max_pages: int):
        self.reader = reader
        self._max_pages = max_pages  # Managed attribute

    @property
    def max_pages(self) -> int:
        return self._max_pages

    @max_pages.setter
    def max_pages(self, value: int):
        if value < 0:
            raise ValueError("Максимальное количество страниц не может быть отрицательным.")
        self._max_pages = value

    @abstractmethod
    def calculate_statistics(self) -> dict:
        pass

    def __str__(self):
        return f"Subscription for {self.reader.name}"

    def __repr__(self):
        return f"<Subscription(reader={self.reader}, max_pages={self.max_pages})>"


class FreeSubscription(Subscription):
    def calculate_statistics(self) -> dict:
        total_pages = self.reader.total_pages_read
        remaining_pages = max(0, self.max_pages - total_pages)
        return {
            "total_pages_read": total_pages,
            "remaining_pages": remaining_pages,
            "subscription_type": "Free",
        }

    def __str__(self):
        return f"FreeSubscription for {self.reader.name}, max_pages={self.max_pages}"

    def __repr__(self):
        return f"<FreeSubscription(reader={self.reader}, max_pages={self.max_pages})>"


class PaidSubscription(Subscription):
    def calculate_statistics(self) -> dict:
        total_pages = self.reader.total_pages_read
        return {
            "total_pages_read": total_pages,
            "subscription_type": "Paid",
        }

    def __str__(self):
        return f"PaidSubscription for {self.reader.name}"

    def __repr__(self):
        return f"<PaidSubscription(reader={self.reader})>"
