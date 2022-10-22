from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT", callback_data='button_call1')
    markup.add(button_call1)

    question = 'Как называется единственная река, вытекающая из озера Байкал?'
    answers = [
        'Обь',
        'Ангара',
        'Енисей',
        'Амур'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Не шаришь',
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/membot.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.from_user.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.from_user.id, 'Сообщение должно быть ответом')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
