from datetime import datetime

from models.core_classes import Updateable


class Game(Updateable):
    id: int

    game_date: datetime

    visitors: int
    result: str

    stadium: int
    players: list[int]

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.game_date = datetime.strptime(kwargs["game_date"], "%d-%m-%Y")
        self.visitors = kwargs["visitors"] if kwargs.get("visitors") else 0
        self.result = "0-0"
        self.stadium = kwargs["stadium"]
        self.players = kwargs["players"]

    def __repr__(self):
        return f"Game: id={self.id}, {self.result=} at date: {str(self.game_date)}"


