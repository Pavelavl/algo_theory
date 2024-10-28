from abc import ABC, abstractmethod
from .reader import Reader

class Subscription(ABC):
    def __init__(self, reader: Reader, max_pages: int):
        self.reader = reader
        self.max_pages = max_pages

    @abstractmethod
    def calculate_statistics(self) -> dict:
        pass

    def __str__(self):
        return f"Subscription for {self.reader.name}"

class FreeSubscription(Subscription):
    def calculate_statistics(self) -> dict:
        total_pages = self.reader.total_pages_read
        remaining_pages = max(0, self.max_pages - total_pages)
        return {
            "total_pages_read": total_pages,
            "remaining_pages": remaining_pages,
            "subscription_type": "Free",
        }

class PaidSubscription(Subscription):
    def calculate_statistics(self) -> dict:
        total_pages = self.reader.total_pages_read
        return {
            "total_pages_read": total_pages,
            "subscription_type": "Paid",
        }
