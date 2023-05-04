from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from code.internal import commands_st
from code.generated.context import ctx


router = Router()


@router.message(Command(commands_st.start.command))
async def cmd_start(message: Message):
    await message.answer(ctx.tanker.start)
