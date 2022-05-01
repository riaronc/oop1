from models.core_classes import Stack
from models.game import Game


class Stadium(Updateable):
    id: int
    capacity: int
    price_per_seat: float

    games: Stack[Game]
