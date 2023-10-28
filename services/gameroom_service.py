from typing import List, Dict, Set

from enums.GameEnums import GameStateEnum, GameTimeEnum
from enums.PlayerEnums import PlayerRoleEnum
from models import UserModel, PlayerModel
from models.room_model import RoomModel
from repositories import GameRepository


# this service manage current game room
class GameRoomService:
    def __init__(self, room_number: int):
        self._repository: GameRepository = GameRepository()
        self.room: RoomModel = self._repository.create_room(room_number)

        self.by_roles: Dict[PlayerRoleEnum, List[PlayerModel]] = dict()
        self.by_roles[PlayerRoleEnum.peaceful] = list()
        self.by_roles[PlayerRoleEnum.mafia] = list()

        #self.roles: Set[PlayerRoleEnum] = set()

    def is_started(self):
        return self.room.is_started

    def is_waiting_for_players(self):
        return not self.room.is_started and not self.room.is_ended

    def next_move(self) -> None:
        pass

    def add_player(self, user: UserModel) -> None:
        player = PlayerModel(self.room.number, user)
        self.room.players.append(player)

    def distribute_roles(self) -> None:
        pass
