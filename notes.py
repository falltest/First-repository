from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from keyboards import *
n = 1
from Telegram_bot import *
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
def count_slov(s):
    s = s + ' '
    angl = set('qwertyuiopasdfghjklzxcvbnm')
    russ = set('ёйцукенгшщзхъфывапролдячсмитьбюжэ')
    count = 0
    word = ''
    for c in s:
        if c in angl or c in russ:
            word += c
        else:
            if word != '':
                count += 1
            word = ''
    return count
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))

n += 1
@dp.callback_query_handler(lambda c: c.data == f'Заметка {n}', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    name = notes_buttons[1].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(count_slov(d[name]))