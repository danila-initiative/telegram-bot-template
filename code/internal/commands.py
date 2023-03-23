from aiogram import types


class CommandsST:
    start: types.BotCommand

    def __init__(self):
        self.start = types.BotCommand(command='start', description='Start bot')


commands_st = CommandsST()
