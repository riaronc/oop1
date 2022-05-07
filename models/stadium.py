from models.core_classes import Updateable


class Stadium(Updateable):
    id: int
    capacity: int
    price_per_seat: float

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.capacity = kwargs["capacity"]
        self.price_per_seat = kwargs["price_per_seat"]

    def __repr__(self):
        return f"Stadium id={self.id}"
