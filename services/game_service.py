from typing import List, Dict, Set

from enums.GameEnums import GameStateEnum, GameTimeEnum
from enums.PlayerEnums import PlayerRoleEnum
from models import UserModel, PlayerModel


# this service manage current game room
class GameService:
    def __init__(self, room_number: int):
        self.room_number: int = room_number
        self.is_started: bool = False
        self.is_ended: bool = False
        self.players: List[PlayerModel] = list()
        self.by_roles: Dict[PlayerRoleEnum, List[PlayerModel]] = dict()
        self.by_roles[PlayerRoleEnum.peaceful] = list()
        self.by_roles[PlayerRoleEnum.mafia] = list()

        self.state: GameStateEnum = GameStateEnum.meeting
        self.time: GameTimeEnum = GameTimeEnum.day
        self.roles: Set[PlayerRoleEnum] = set()

    def next_move(self) -> None:
        pass

    def add_player(self, user: UserModel) -> None:
        player = PlayerModel(self.room_number, user)
        self.players.append(player)

    def distribute_roles(self) -> None:
        pass
