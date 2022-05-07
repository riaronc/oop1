from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    items: list[T]

    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def delete(self, id) -> T:
        i = self.find(id=id)
        return self.items.pop(i)

    def show_all(self) -> None:
        for item in self.items:
            print(item)

    def find(self, id) -> T:
        id = int(id)
        for i in range(len(self.items)):
            if id == self.items[i].id:
                return i
        return None


class Updateable:
    def update(self, **kwargs):
        self.update(**kwargs)
