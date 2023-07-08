from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

active_users = []
@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Привет, как тебя зовут?")
    await state.set_state("name")

@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name" : name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await state.set_state("echo")


@dp.message_handler(state="echo")
async def echo_handler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'{user_data["name"]} сказал: {message.text}. Было бы еще круче если бы {user_data["name"]} сказал сколько ему лет.')
    await state.set_state("age")

#await bot.send_message(chat_id=id, text='n')
@dp.message_handler(state="age")
async def age_handler(message: types.Message, state: FSMContext):
    if int(message.text) < 18:
        await message.answer('Увы, но этого бота нельзя использовать лицам меньше 18 лет.')
    else:
        await message.answer('Напишите /find для поиска собеседника и /stop для прекращения разговора')
    await state.set_state("chat_start")


@dp.message_handler(commands=['stop'], state="chat_start")
async def error_stop_handler(message: types.Message, state: FSMContext):
    """Ошибка, когда ты не в диалоге"""
    await message.answer('Вы не в диалоге')


@dp.message_handler(commands=['find'], state="chat_start")
async def start_handler(message: types.Message, state: FSMContext):
    id = message.from_user.id
    active_users.append(id)
    await message.answer('Ожидайте')
    if len(active_users) == 2:
        await bot.send_message(active_users[0], text="Собеседник найден")
        await bot.send_message(active_users[1], text="Собеседник найден")
        await state.set_state("chat_is_starting1")

@dp.message_handler(state="chat_is_starting1")
async def starting1_handler(message: types.Message, state: FSMContext):
    id2 = active_users[1]
    if message.text == '/stop':
        await bot.send_message(chat_id=id2, text="Ваш собеседник остановил чат.")
        active_users = set(active_users)
        active_users.discard(id2)
        active_users = list(active_users)
        await state.set_state("chat_stop")
    else:
        await bot.send_message(chat_id=id2, text=message.text)

@dp.message_handler(state="chat_is_starting2")
async def starting2_handler(message: types.Message, state: FSMContext):
    id1 = active_users[0]
    if message.text == '/stop':
        await bot.send_message(chat_id=id1, text="Ваш собеседник остановил чат.")
        active_users = set(active_users)
        active_users.discard(id1)
        active_users = list(active_users)
        await state.set_state("chat_stop")
    else:
        await bot.send_message(chat_id=id1, text=message.text)

@dp.message_handler(commands=['find'], state="chat_stop")
async def error_find_handler(message: types.Message, state: FSMContext):
    """Ошибка по время диалога"""
    await message.answer('Вы можете только остановить диалог')

@dp.message_handler(state="chat_stop")
async def stop_handler(message: types.Message, state: FSMContext):
    await message.answer('Напишите /find для поиска собеседника и /stop для прекращения разговора.')
    await state.set_state('chat_start')
'''
@dp.message_handler(state='chat')
async def chatting(message: types.Message, state: FSMContext):
    await 
'''
executor.start_polling(dp, skip_updates=True)