from datetime import datetime

from models.core_classes import Updateable
from models.stadium import Stadium
from models.core_classes import Stack
from models.player import Player



class Game(Updateable):
    id: int

    game_date: datetime

    visitors: int
    result: str

    stadium: int
    players: list[int]

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.game_date = datetime.strptime(kwargs["game_date"], "%Y-%m-%d")
        self.visitors = kwargs["visitors"] if kwargs.get("visitors") else 0
        self.result = "0-0"
        self.stadium = kwargs["stadium"]
        self.players = kwargs["players"]


