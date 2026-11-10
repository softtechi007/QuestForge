class Inventory:
    def __init__(self):
        self._items: list = []


    def add(self, item) -> None:
        self._items.append(item)


    def use(self, index: int, target) -> str:
        item = self._items.pop(index)
        return item.apply(target)


    def list_items(self) -> list[str]:
        return [type(i).__name__ for i in self._items]