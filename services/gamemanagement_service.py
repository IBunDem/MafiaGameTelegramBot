from typing import List, Tuple

from utils import locator
from models import UserModel
from models.room_model import RoomModel
from repositories import MainRepository
from services.gameroom_service import GameRoomService


# This service manage game rooms
class GameManagementService:
    def __init__(self):
        self.__repository: MainRepository = locator.get(MainRepository)
        self.last_number: int = 0

        self.rooms: List[GameRoomService] = list()

    def create_room(self) -> RoomModel:
        game = GameRoomService(self.last_number)
        self.last_number += 1
        self.rooms.append(game)

        return game

    def _get_waiting_rooms(self) -> List[GameRoomService]:
        waiting_rooms = list(filter(lambda room: room.is_waiting_for_players(), self.rooms))
        return waiting_rooms

    def add_player_to_room(self, user: UserModel) -> None:
        from exceptions import UserNotRegisteredException

        self._get_waiting_rooms()

        # If here is not any waiting for players room create a new
        if not any(self._get_waiting_rooms()):
            self.create_room()

        first_room = self._get_waiting_rooms()[0]
        first_room.add_player(user)

    def start_game_at_room(self, room_number: int) -> None:
        pass
