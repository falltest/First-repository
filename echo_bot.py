from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Ловецб обработчик сообщений"""
    await message.answer("Добро пожаловать в тестового бота")

'''
@dp.message_handler()
async def echo_answer(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(commands=['catphoto'])
async def photo_of_cat(message: types.Message):
    with open('cat.jpg', 'rb') as f:
        #await message.answer("Добро пожаловать в тестового бота2")
        await message.answer_photo(f)
        f.close()
'''
d = {}
@dp.message_handler(commands=['startnewnotes'])
async def start_notes(message: types.Message):
    """Записывает первую заметку"""
    #global d
    await message.answer('Напишите ваше имя')

@dp.message_handler()
async def echo_answer(message: types.Message):
    await message.answer('Перемещаю вас в чат...')










executor.start_polling(dp, skip_updates=True)