from code.internal.config import context

import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from code.handlers import start
from code.internal import commands_st

TOKEN = context.user_bot_token.get_secret_value()


# Запуск бота
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    routes = (start,)
    for route in routes:
        dp.include_router(route.router)

    await bot.set_my_commands(commands_st.rating)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
