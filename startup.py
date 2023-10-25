from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from controllers import *


async def startup() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.include_router(player_router)
    dp.include_router(test_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
