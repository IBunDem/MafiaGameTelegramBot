from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

player_router: Router = Router()


@player_router.message(Command('play'))
async def player_play(msg: Message):
    await msg.answer('Ну давай же сыграем!')
