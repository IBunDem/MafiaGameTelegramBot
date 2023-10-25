from enums.GameEnums import GameStateEnum, GameTimeEnum


class GameService:
    def __init__(self):
        self.room_number = 0
        self.is_started = False
        self.is_ended = False
        self.players = list()
        self.state = GameStateEnum.none
        self.time = GameTimeEnum.day
        self.roles = list()

    def next_move(self):
        pass

    def add_player(self):
        pass

    def distribute_roles(self):
        pass

    def done(self):
        pass