from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from code.internal import commands_st


router = Router()


@router.message(Command(commands_st.start.command))
async def cmd_start(message: Message):
    await message.answer("Using this bot you could do something.")
