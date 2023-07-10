from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from keyboards import *
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

da = KeyboardButton('Да')
net = KeyboardButton('Нет')
count = 0
click = InlineKeyboardButton("click!", callback_data='click')
click_keyboard = InlineKeyboardMarkup().insert(click)
da_net_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(da).add(net)


@dp.message_handler(commands=['start'], state='*')
async def name_handler(message: types.Message, state: FSMContext):
    await message.answer('Готовы?', reply_markup=da_net_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'click')
async def about_bot_message(callback_query: types.CallbackQuery):
    global count
    count += 1

@dp.message_handler(commands=['count'],state='*')
async def about_bot_message(message: types.Message, state: FSMContext):
    await message.answer(f'Вы нажали {count} раз!')
 
@dp.message_handler(state='*')
async def name_handler(message: types.Message, state: FSMContext):
    if message.text == 'Нет':
        await message.answer('Напишите /start когда будете готовы')
    elif message.text == 'Да':
        await message.answer('Click!!!', reply_markup = click_keyboard)

executor.start_polling(dp, skip_updates=True)