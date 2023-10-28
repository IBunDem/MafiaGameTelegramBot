from typing import List, Tuple, Union

from aiogram.types import Message

from exceptions.main_exceptions import UserAlreadyRegisteredException
from models import UserModel


class MainRepository:
    def __init__(self):
        self.users: List[UserModel] = list()

    def register_user(self, chat_id: int, username: str, fullname: str) -> UserModel:
        # check if same user already registered
        if any(filter(lambda u: u.chat_id == chat_id, self.users)):
            raise UserAlreadyRegisteredException(f'User with id {chat_id} already is registered')

        user = UserModel(chat_id, username, fullname)
        self.users.append(user)
        return user

    def register_user_from_msg(self, msg: Message) -> UserModel:
        return self.register_user(msg.chat.id, msg.chat.username, msg.chat.full_name)

    def get_user_by_chat_id(self, chat_id) -> Union[UserModel, None]:
        filtered: Tuple[UserModel] = tuple(filter(lambda u: u.chat_id, self.users))
        if not any(filtered): return None
        return filtered[0]
