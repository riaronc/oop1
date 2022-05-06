from controllers.commands import parse_data
from models.core_classes import Stack
from models.game import Game
from models.player import Player
from models.stadium import Stadium
from tools import app_setup


class App:
    filename: str
    games: Stack[Game]
    players: Stack[Player]
    stadiums: Stack[Stadium]

    def __init__(self, filename: str = "test_data.json"):
        self.filename = filename

    def run(self):
        data = app_setup.read_the_file(filename=self.filename)
        self.games = parse_data(data.get("games"), class_=Game)
        self.players = parse_data(data.get("players"), class_=Player)
        self.stadiums = parse_data(data.get("stadiums"), class_=Stadium)
        while True:
            print('Input the command:')
            self.execute_command(input())

    def execute_command(self, command: str):
        models = {'players': self.players, 'games': self.games, 'stadiums': self.stadiums}
        actions = ('list', 'create', 'delete')

        if command not in actions:
            print(f"Available commands: {actions}")
            return

        print(f"Choose the model: {list(models.keys())}")
        model = input()
        if model not in models.keys():
            print("Bad model")
            return
