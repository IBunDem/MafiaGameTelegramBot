from typing import List

from models.room_model import RoomModel


class GameRepository:
    def __init__(self):
        self.rooms: List[RoomModel] = list()

    def create_room(self, room_number: int) -> RoomModel:
        room = RoomModel(room_number)
        self.rooms.append(room)

        return room
