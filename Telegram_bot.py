from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from keyboards import *
#from googletrans import Translator
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
d = {}
notes_buttons = []
name_of_new_note = ''
main_menu = {'text': 'Что вам нужно в данный момент?', 'reply_markup': keyboard_markup}
menu_of_notes = {'text': '', 'reply_markup': ''}


@dp.message_handler(commands='start',state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.reply("Напишите ваше имя...")
    await state.set_state('buttons')

@dp.message_handler(state='buttons')
async def buttons_message(message: types.Message, state: FSMContext):
    """Выдает список возможных действий: Заметки, библиотека ссылок"""
    global name
    name = message.text
    await state.update_data({'name' : name})
    await state.set_state('change_notes')
    await message.answer(f'Привет, {name}!')
    await message.answer(**main_menu)

@dp.callback_query_handler(lambda c: c.data == 'notes', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Выдает список заметок, чтобы изменить"""
    global d
    global notes_buttons
    global menu_of_notes
    if add_button not in notes_buttons:
        notes_buttons.append(add_button)
        notes_keyboard = InlineKeyboardMarkup()
        notes_keyboard.row(add_button)
    elif len(notes_buttons) >= 2:
        notes_keyboard = InlineKeyboardMarkup()
        for i in notes_buttons:
            notes_keyboard.row(i)
    #await call.answer('Как вы хотите назвать журнал заметок?', True)
    await call.message.edit_text('123', reply_markup=notes_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'add_note', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Принимает команду создания новой заметки"""
    global d
    await call.answer('Напиши название будующей заметки...', True)
    await state.set_state('name_of_new_note')

@dp.message_handler(state='name_of_new_note')
async def about_bot_message(message: types.Message, state: FSMContext):
    """Принимает имя новой заметки"""
    global d
    d[message.text] = ''
    global name_of_new_note
    global notes_buttons
    name_of_new_note = message.text
    new_button = InlineKeyboardButton(name_of_new_note, callback_data='change_note')
    notes_buttons.append(new_button)
    await state.set_state('value_of_new_note')
    await message.answer('Что хочешь записать в заметку?')

@dp.message_handler(state='value_of_new_note')
async def about_bot_message(message: types.Message, state: FSMContext):
    """Записывает заметку"""
    global d
    d[name_of_new_note] = message.text
    await message.answer('Заметка записана!')
    await message.answer(**main_menu)

@dp.callback_query_handler(lambda c: c.data == 'change_note', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Возможные действия с существующей заметкой"""
    global d
    await call.message.edit_text('Вы хотите...', reply_markup=change_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'change_name', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Меняет имя заметки"""
    global d
    print(call.get_current())

'''
@dp.message_handler()
async def send_message(msg: types.Message):
    await msg.reply("Привет!")
'''

'''
@dp.callback_query_handler(lambda c: c.data == 'Заметка')
async def about_bot_message(call: types.CallbackQuery):
    """Меняет конкретную заметку"""
    global d
    await call.answer('Ты нажал на кнопку!', True)
'''


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
