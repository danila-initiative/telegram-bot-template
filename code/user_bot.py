import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from code.handlers import start
from code.generated.context import ctx  # type: ignore


# Запуск бота
async def main():
    bot = Bot(token=ctx.env.user_bot_token.get_secret_value())
    dp = Dispatcher()

    routes = (start,)
    for route in routes:
        dp.include_router(route.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
