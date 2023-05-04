from aiogram import Bot

from code.generated.context import ctx


async def send(text: str, chat_ids: list[int]):
    bot = Bot(token=ctx.env.user_bot_token.get_secret_value())

    for chat_id in set(chat_ids):
        await bot.send_message(chat_id=chat_id, text=text)

    await bot.close()
