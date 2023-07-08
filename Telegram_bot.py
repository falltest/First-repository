from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def echo_answer(message: types.Message):
    await message.answer("Приветсвую в нашем телеграм боте. Он поможет вам написать сочинения, поможет проверить грамотность, перевести слова и выражения. Какое у вас имя?")

@dp.message_handler(state="notes")
async def name_handler(message: types.Message, state: FSMContext):
    await message.answer('Вы хотите добавить новую заметку или изменить старую?')
