from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from keyboards import *
from googletrans import Translator
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

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
    await message.reply(f'Привет, {name}! Я бот, который поможет вам написать сочинения.\nЧто вам нужно в данный момент?', reply_markup=keyboard_markup)

'''
@dp.message_handler()
async def send_message(msg: types.Message):
    await msg.reply("Привет!")
'''
d = {}
@dp.callback_query_handler(lambda c: c.data == 'notes')
async def about_bot_message(call: types.CallbackQuery):
    """Выдает список заметок, чтобы изменить"""
    global d
    notes_buttons = []
    n = 1
    notes_keyboard = InlineKeyboardMarkup()
    for i in d:
        await notes_buttons.append(f'заметка №{n}', callback_data = 'Заметка')
        n += 1
    if len(notes_buttons) > 0:
        for i in notes_buttons:
            notes_keyboard.row(i)
    else:
        await call.answer('У тебя нет заметок для изменений', True)

@dp.callback_query_handler(lambda c: c.data == 'Заметка')
async def about_bot_message(call: types.CallbackQuery):
    """Меняет конкретную заметку"""
    global d

    await call.answer('Ты нажал на кнопку!', True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
