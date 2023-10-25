from aiogram import Router
from aiogram.types import Message

test_router = Router()


@test_router.message()
async def echo_msg(msg: Message):
    await msg.answer(f"Сообщение принято, {msg.chat.username}. Или лучше сказать, {msg.chat.full_name}")

