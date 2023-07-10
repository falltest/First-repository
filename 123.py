from __future__ import annotations
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
count = 0


@dp.message_handler(commands=['start'], state='*')
async def name_handler(message: types.Message, state: FSMContext):
    await state.set_state('first_q')
    await message.answer('Приветствуем в нашей викторине! Вы готовы начать?', reply_markup=da_net)


@dp.message_handler(state='first_q')
async def name_handler(message: types.Message, state: FSMContext):
    await state.set_state('second_q')
    if message.text == 'Да':
        await message.answer('Отлично, тогда мой первый вопрос: у списков есть индексы?', reply_markup=da_net)
    else:
        await message.answer("Напишите комманду /start когда будете готовы")


@dp.message_handler(state='second_q')
async def name_handler(message: types.Message, state: FSMContext):
    await state.set_state('third_q')
    if message.text == 'Да':
        global count
        count += 1
        await message.answer('Ладно, это было легко. Следущий вопрос: Почему?', reply_markup=pochemu_net)
    else:
        await message.answer("Увы увы. Следущий вопрос: Почему?", reply_markup=pochemu_net)


@dp.message_handler(state='third_q')
async def name_handler(message: types.Message, state: FSMContext):
    await state.set_state('result')
    if message.text == 'Потому':
        global count
        count += 1
        await message.answer('Да, правильно. Хотите увидеть результаты?', reply_markup=da_net)
    else:
        await message.answer("Эх... Хотите увидеть результаты?", reply_markup=da_net)


@dp.message_handler(state='result')
async def name_handler(message: types.Message, state: FSMContext):
    await state.set_state('*')
    if message.text == 'Да':
        await message.answer(f'У вас {count} правильных ответов!')
    else:
        await message.answer("Ну ладно")


count = 0

executor.start_polling(dp, skip_updates=True)
