from datetime import datetime

from models.core_classes import Stack
from models.core_classes import Updateable
from models.player import Player
from models.stadium import Stadium


class Game(Updateable):
    id: int

    game_date: datetime
    stadium: Stadium
    visitors: int
    result: str

    players: Stack[Player]
