from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from repositories import MainRepository
from services.gamemanagement_service import GameManagementService
from utils import locator

player_router: Router = Router()


@player_router.message(Command('play'))
async def player_play(msg: Message):
    game_manager: GameManagementService = locator.get(GameManagementService)
    main_repository: MainRepository = locator.get(MainRepository)

    user = main_repository.get_user_by_chat_id(msg.chat.id)
    if not user:
        user = main_repository.register_user_from_msg(msg)
        await msg.answer('Теперь Вы зарегистрированы в нашем городке.')

    game_manager.add_player_to_room(user)
    await msg.answer('Вы добавлены в комнату, дождёмся ещё игроков и начнём')


@player_router.message(Command('status'))
async def palyer_status(msg: Message):
    main_repository: MainRepository = locator.get(MainRepository)

    user = main_repository.get_user_by_chat_id(msg.chat.id)
    await msg.answer('Beeep')
