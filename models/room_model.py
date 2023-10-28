from typing import List, Set

from enums.GameEnums import GameStateEnum, GameTimeEnum
from enums.PlayerEnums import PlayerRoleEnum
from models import PlayerModel


class RoomModel:
    def __init__(self, number: int):
        self.number: int = number
        self.players: List[PlayerModel] = list()
        self.is_started: bool = False
        self.is_ended: bool = False

        self.state: GameStateEnum = GameStateEnum.meeting
        self.time: GameTimeEnum = GameTimeEnum.day
