from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
name = ''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message, state: FSMContext):
    await message.reply("Напишите ваше имя...")
    await state.set_state('name')

@dp.message_handler(state='name')
async def name_message(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name' : name})
    await message.answer(f'Привет {name}!')
    await state.set_state('buttons')

@dp.message_handler(state='buttons')
async def buttons_message(message: types.Message, state: FSMContext):
    keyboard_markup = types.InlineKeyboardMarkup()
    notes = types.InlineKeyboardButton('Заметки', callback_data= 'press')
    link_library = types.InlineKeyboardButton('Библиотека ссылок', callback_data= 'press')
    keyboard_markup.row(notes, link_library)
    await message.reply("Привет!\Я бот, который поможет вам написать сочинения!\nЧто вам нужно в данный момент?", reply_markup=keyboard_markup)

'''
@dp.message_handler()
async def send_message(msg: types.Message):
    await msg.reply("Привет!")
'''
@dp.callback_query_handler(lambda c: c.data == 'press')
async def about_bot_message(call: types.CallbackQuery):
    await call.answer('Ты нажал на кнопку!', True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)