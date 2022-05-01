from models.core_classes import Updateable


class Player(Updateable):
    id: int
    first_name: str
    last_name: str
    birth_date: str
    status: str
    health: str
    salary: float
