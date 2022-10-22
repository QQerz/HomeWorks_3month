from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
from random import choice


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('game'):
        if message.from_user.id in ADMINS:
            await bot.send_dice(message.from_user.id, emoji=choice(['🎰', '🎳', '🎯', '🎲', '⚽', '🏀']))
        else:
            await bot.send_message(message.from_user.id, 'Ты не админ')
    else:
        if message.text.isnumeric():
            a = int(message.text)
            await bot.send_message(message.chat.id, a ** 2)
        else:
            await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
