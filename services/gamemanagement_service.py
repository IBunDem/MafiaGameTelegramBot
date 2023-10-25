from typing import List

from services.game_service import GameService


# This service manage game rooms
class GameManagementService:
    def __init__(self):
        self.last_number: int = 0

        self.games: List[GameService] = list()
        self.waiting_for_users_games: List[GameService] = list()
        self.stated_games: List[GameService] = list()

    def create_game(self) -> None:
        game = GameService(self.last_number)
        self.last_number += 1
        self.games.append(game)

    def add_player_to_room(self) -> None:
        pass

    def start_game_at_room(self, room_number: int) -> None:
        pass
