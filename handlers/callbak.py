from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


# @dp.callback_query_handler(lambda call: call.data == "button_call1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("NEXT", callback_data='button_call2')
    markup.add(button_call2)

    question = 'Какова должна быть высота возвышенности, чтобы ее можно было назвать горой?'
    answers = [
        '100 метров',
        '150 метров',
        '200 метров',
        '250 метров'

    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Не шаришь',
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Основатель Apple"
    answers = [
        'Цукерберг',
        'Стив Джобс',
        'Илон Маск'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Не шаришь'
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call2')
