from __future__ import annotations
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import keyboards
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
main_menu = {"text" : "Узнать расписание автобуса",
             "reply_markup" : keyboards.busses_keyboard}
@dp.message_handler(commands=['start'],state='*')
async def process_start(message: types.Message, state: FSMContext):
    await message.answer(**main_menu)
@dp.callback_query_handler(lambda c: c.data == 'bus108', state='*')
async def process_bus_108(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_reply_markup(keyboards.back_keyboard)
@dp.callback_query_handler(lambda c: c.data == 'bus106', state='*')
async def process_bus_108(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text('Автобус 106 сейчас не работает',
                                           reply_markup=keyboards.back_keyboard)
    
    
@dp.callback_query_handler(lambda c: c.data == 'back', state='*')
async def process_back(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(**main_menu)

@dp.callback_query_handler(state='*')
async def process_error(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(text='Что-то пошло не так...')

executor.start_polling(dp, skip_updates=True)