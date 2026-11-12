from operator import index

from domain.exceptions import InventoryEmptyError

class Inventory:
    def __init__(self):
        self._items: list = []


    def add(self, item) -> None:
        self._items.append(item)


    def use(self, index: int, target) -> str:
        try:
            # Try to remove and get the item in one step
            item = self._items.pop(index) 
            return item.apply(target)        
        except IndexError:
            # This is indented ONE level inside the except
            raise InventoryEmptyError(f"Cannot use item at index {index}. Inventory is empty or invalid.")


    def list_items(self) -> list[str]:
        return [type(i).__name__ for i in self._items]