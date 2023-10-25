class UserModel:
    def __init__(self, chat_id: int, username: str, fullname: str):
        self.chat_id: int = chat_id
        self.username: str = username
        self.fullname: str = fullname
