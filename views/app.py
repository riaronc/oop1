from controllers.main_controller import *
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
        self.games = app_setup.parse_data(data.get("games"), class_=Game)
        self.players = app_setup.parse_data(data.get("players"), class_=Player)
        self.stadiums = app_setup.parse_data(data.get("stadiums"), class_=Stadium)
        while True:
            self.execute_command()

    def execute_command(self):
        models = {'players': self.players, 'games': self.games, 'stadiums': self.stadiums}
        print(f"Choose the model: {list(models.keys())}")

        selected_model = None
        class_ = None
        while not selected_model and not class_:
            model = self.get_input()
            match model:
                case "players":
                    selected_model = self.players
                    class_ = Player
                case "games":
                    selected_model = self.games
                    class_ = Game
                case "stadiums":
                    selected_model = self.stadiums
                    class_ = Stadium
                case _:
                    print(f"Choose the model: {list(models.keys())}")

        commands = ('list', 'create', 'delete')
        print(f"Choose the command: {commands}")
        command = self.get_input()

        if command not in commands:
            print(f"Available commands: {commands}")
            return

        match command:
            case "list":
                selected_model.show_all()
            case "create":
                create_new_entity(entity=selected_model, class_=class_)
            case "delete":
                delete_selected_entity(entity=selected_model)
            case "find":
                find_selected_entity(entity=selected_model)

    def get_input(self):
        input_ = input()
        if input_.lower() == 'exit':
            self.save_data()
            print("All data is successfully saved")
            exit()

        return input_

    def save_data(self):
        result = {}
        result["stadiums"] = {vars(s) for s in self.stadiums.items}
        result["players"] = {vars(s) for s in self.players.items}
        result["games"] = {vars(s) for s in self.games.items}
        with open(self.filename, 'w') as file:
            file.write(str(result))
            print("Successfully saved all the data")
