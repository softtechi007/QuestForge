from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def apply(self, character) -> str:
        """Apply this item's effect to a character; return a description string."""