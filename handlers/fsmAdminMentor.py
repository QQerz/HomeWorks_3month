from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, ADMINS
from keyboard.client_cb import cancel_markup, submit_markup


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMINS and message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer('Введите айди ментора', reply_markup=cancel_markup)
    elif message.from_user.id not in ADMINS:
        await message.answer('Ты не АДМИН!')
    else:
        await message.answer('Пиши в личку')


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Имя ментора?', reply_markup=cancel_markup)
    except:
        await message.answer('Неправильное айди', reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Направление ментора', reply_markup=cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора', reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Группа ментора', reply_markup=cancel_markup)
    except:
        await message.answer('Неправильный возраст', reply_markup=cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await bot.send_message(message.chat.id, f"ID - {data['id']}\nName -  {data['name']}\nDirection - {data['direction']}"
                                                f"\nAge - {data['age']}, Group - {data['group']}")
    await FSMAdmin.next()
    await message.answer('Всё правильно?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # Запись в БД
        await state.finish()
        await message.answer('Регистрация завершена')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('Ошибка')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals='Cancel'), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)