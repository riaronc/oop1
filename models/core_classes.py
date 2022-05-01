from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def delete(self) -> T:
        return self.items.pop()

    def show_all(self) -> None:
        for item in self.items:
            print(item)

    def find(self, id) -> T:
        for item in self.items:
            if id == item.id:
                return item
        return None


class Updateable:
    def update(self, **kwargs):
        self.update(**kwargs)
