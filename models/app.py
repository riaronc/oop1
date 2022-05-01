from tools import app_setup
from models.game import Game
from models.player import Player
from models.stadium import Stadium
from models.core_classes import Stack



class App:
    filename: str
    games: Stack[Game]
    players: Stack[Player]
    stadiums: Stack[Stadium]


    def __init__(self, filename):
        self.filename = filename
        self.start()

    def start(self):
        app_setup.read_the_file(filename=self.filename)
