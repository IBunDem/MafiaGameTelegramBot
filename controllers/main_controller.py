from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from repositories import MainRepository

main_router = Router()
repository = MainRepository()


@main_router.message(Command('start'))
async def register(msg: Message):
    from exceptions.main_exceptions import UserAlreadyRegisteredException

    try:
        user = repository.register_user_from_msg(msg)
        name = user.fullname if user.fullname.strip() != '' else user.username
        await msg.answer(f'Добро пожаловать в наш город, {name}! Надеюсь, ты будешь почаще выживать!')
    except UserAlreadyRegisteredException as ex:
        await msg.answer('Пройдоха, ты уже у нас зарегистрирован!')
