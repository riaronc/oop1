from models.core_classes import Updateable


class Player(Updateable):
    id: int
    first_name: str
    last_name: str
    birth_date: str
    status: str
    health: str
    salary: float

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.birth_date = kwargs["birth_date"]
        self.status = kwargs["status"]
        self.health = kwargs["health"]
        self.salary = kwargs["salary"]
