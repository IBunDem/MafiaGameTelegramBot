from aiogram import Bot

from models import UserModel


class BotAnswerService:
    def __init__(self, bot: Bot):
        self.bot: Bot = bot

    async def send_message(self, user: UserModel, message_text: str) -> None:
        await self.bot.send_message(user.chat_id, text=message_text)
