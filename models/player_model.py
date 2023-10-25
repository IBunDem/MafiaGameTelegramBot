from models.user_model import UserModel


class PlayerModel:
    def __init__(self, user: UserModel):
        self.user = user
        self.role = None
        self.is_alive = False
