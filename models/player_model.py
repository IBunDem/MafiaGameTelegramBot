from enums.PlayerEnums import PlayerRoleEnum
from models.user_model import UserModel


class PlayerModel:
    def __init__(self, room_number: int, user: UserModel):
        self.room_number: int = room_number
        self.user: UserModel = user
        self.role: PlayerRoleEnum = PlayerRoleEnum.none
        self.is_alive: bool = True

    def set_role(self, role: PlayerRoleEnum) -> None:
        self.role = role

    def kill(self) -> None:
        self.is_alive = False

