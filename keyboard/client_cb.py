from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
).add(cancel_button)


submit_markup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
).add(KeyboardButton('Да'), KeyboardButton('Нет'))