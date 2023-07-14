from __future__ import annotations
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup
from googletrans import Translator
translator1212 = Translator()
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
from keyboards import *
import requests
import urllib.request
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
d = {}
notes_buttons = []
name_of_new_note = ''
main_menu = {'text': 'Что вам нужно в данный момент?', 'reply_markup': keyboard_markup}
menu_of_notes = {'text': '', 'reply_markup': ''}
last_content = ''
last_name = ''
count_of_cats = 0


@dp.message_handler(commands='start',state='*')
async def start_handler(message: types.Message, state: FSMContext):
    '''Запрашивает имя пользователя'''
    await message.reply("Напишите ваше имя...")
    await state.set_state('buttons')

@dp.message_handler(commands='catphoto',state='*')
async def start_handler(message: types.Message, state: FSMContext):
    '''Отправляет рандомного котенка'''
    global count_of_cats
    count_of_cats += 1
    url = 'https://api.thecatapi.com/v1/images/search?limit=10'
    response = requests.get(url).json()
    url_cat = ''
    for data in response:
        url_cat = data['url']
    file = open(f'cat.jpg', 'wb') # write bytes
    file.write(
        requests.get(url_cat).content
        )
    file.close()
    id_user = message.from_user.id
    await bot.send_photo(chat_id = id_user, photo=open('cat.jpg', 'rb'))

#result = translator.translate('hello world', src='en', dest='ru')
@dp.message_handler(state='buttons')
async def buttons_message(message: types.Message, state: FSMContext):
    """Выдает список возможных действий: Заметки, библиотека ссылок и переводчик"""
    global name
    name = message.text
    await state.update_data({'name' : name})
    await state.set_state('change_notes')
    await message.answer(f'Привет, {name}!')
    await message.answer(**main_menu)


@dp.callback_query_handler(lambda c: c.data == 'translator', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Принимает текст для перевода"""
    await call.message.answer('Введите текст для перевода на одном из пяти языков:\nФранцузский\nКитайский\nНемецкий\nРусский\nАнглийский')
    await state.set_state('perevod_text')


text = ''
@dp.message_handler(state='perevod_text')
async def buttons_message(message: types.Message, state: FSMContext):
    """Предлагает пользователю перевести текст на один из пяти языков"""
    global text
    global count_of_cats
    text = message.text
    if message.text.lower() == 'i love cats' and count_of_cats == 7:
        id_user = message.from_user.id
        await message.answer('ВЫ НАШЛИ ПАСХАЛКУ ЧТОООО!!!!!!')
        await message.answer(**main_menu)
    else:
        await message.answer('На какой язык вы хотите перевести текст?', reply_markup = languages)
        await state.set_state('perevod')


@dp.message_handler(state='perevod')
async def buttons_message(message: types.Message, state: FSMContext):
    """Переводит текст"""
    global text
    d = {'Русский': 'ru', 'Французский': 'fr', 'Немецкий': 'de', 'Китайский': 'zh-cn', 'Английский': 'en'}
    if message.text in d:
        r = translator1212.detect(text)
        if r.lang == d[message.text]:
            await message.answer('Язык исходного текста и выбранного совпадают, выберите другой язык...')
        else:
            await message.answer(f'Результат: {(translator1212.translate(text, src=r.lang, dest=d[message.text])).text}')
            await message.answer(**main_menu)
    else:
        await message.answer('Такой язык не поддерживается нашим ботом, попробуйте другой')

@dp.callback_query_handler(lambda c: c.data == 'link_library', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Запрашивает задачу для которой пользователь ищет материалы"""
    await call.message.answer('Для какой задачи вы ищете материал?', reply_markup = material)
    await state.set_state('Zad')

@dp.message_handler(state='Zad')
async def start_handler(message: types.Message, state: FSMContext):
    """Ссылки"""
    if message.text == 'Я пишу сочинение, эссе, письменную работу':
        await message.answer('[Брифли](https://briefly.ru/) - сайт поможет вам узнать содержание любой книги, потратив на это минимум времени\n[Образовака](https://obrazovaka.ru/books) - очень схож с брифли\n[Википедия](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0) - это вы и сами знаете что такое\n[Таймер](https://www.timeanddate.com/timer/) который поможет вам уложиться вовремя\n[Ruscorpora](https://ruscorpora.ru/search) - Ресурс, который поможет вам проверить допустимость использования разных слов вместе\n[Грамота.ру](http://gramota.ru/) - Проверит слова на правильность написания', parse_mode='Markdown')
    elif message.text == 'Я хочу перевести текст':
        await message.answer('В данном боте есть функция перевода слов и выражений, но если вам нужен более подробный перевод, то вот некоторые полезные ссылки:')
        await message.answer('[Транслейт.ру](https://www.translate.ru/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4)\n[Гугл переводчик](https://translate.google.com/?hl=ru) - пожалуй, самый популярный переводчик\n[Яндекс переводчик](https://translate.yandex.ru/)\n[Мультитран](https://www.multitran.com/) - переводчик, где есть форум, на которым пользователи могут задачть вопрос или попросить о помощи\n', parse_mode = 'Markdown')
    else:
        await message.answer('Тогда вот некоторые крайне интересные сайты:')
        await message.answer('[Этогочеловеканесуществует](https://www.sravni.ru/goto.ashx?type=ExternalLink&out=https%3A%2F%2Fthispersondoesnotexist.com%2F) - сайт генерирует изображения не сущеcтсвующих людей\n[Радиоооо](https://www.sravni.ru/goto.ashx?type=ExternalLink&out=https%3A%2F%2Fradiooooo.com%2F) - здесь собрана музыка, которую в разное время крутили на радио в разных странах.\n[Геогеср](https://www.sravni.ru/goto.ashx?type=ExternalLink&out=https%3A%2F%2Fwww.geoguessr.com%2F) - ваша задача угадать где находитесь.\n[Драйв & лисен](https://www.sravni.ru/goto.ashx?type=ExternalLink&out=http%3A%2F%2Fdriveandlisten.herokuapp.com%2F) - сайт позволяет кататься на машине в другом городе и случать радио.', parse_mode='Markdown')
@dp.callback_query_handler(lambda c: c.data == 'notes', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Выдает список заметок, чтобы прочитать, удалить или вернуться назад"""
    global d
    global notes_buttons
    global menu_of_notes
    if add_button not in notes_buttons:
        notes_buttons.append(add_button)
        notes_keyboard = InlineKeyboardMarkup()
        notes_keyboard.row(add_button)
        notes_buttons.append(del_button)
        notes_keyboard.row(del_button)
        notes_buttons.append(back_button)
        notes_keyboard.row(back_button)
    elif len(notes_buttons) >= 2:
        notes_keyboard = InlineKeyboardMarkup()
        for i in notes_buttons:
            notes_keyboard.row(i)
    await call.message.edit_text('Вот список заметок:', reply_markup=notes_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'add_note', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Принимает команду создания новой заметки"""
    global d
    global notes_buttons
    if len(notes_buttons) == 12:
        await call.message.answer('Наш бот поддерживает только 10 заметок, пожалуйста удалите какую-то заметку для записи новой')
    else:
        await call.message.answer('Напиши название будующей заметки...')
        await state.set_state('name_of_new_note')


@dp.callback_query_handler(lambda c: c.data == 'back', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Кнопка back"""
    await call.message.answer(**main_menu)


@dp.callback_query_handler(lambda c: c.data == 'delete_note', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    """Кнопка delete_note"""
    await call.message.answer('Напишите название заметки, которую хотите удалить...')
    await state.set_state('delete_note')

@dp.message_handler(state='delete_note')
async def send_message(message: types.Message, state: FSMContext):
    """Принимает имя заметки, которую надо удалить"""
    name = message.text
    global d
    global notes_buttons
    if name in d:
        d.pop(name)
        for i in range(len(notes_buttons) - 2):
            if name == notes_buttons[i].values['text']:
                notes_buttons.pop(i)
        await message.answer('Готово!')
        await message.answer(**main_menu)
    else:
        await message.answer('Такого имени заметки не существует, выберите другое')

@dp.message_handler(state='name_of_new_note')
async def about_bot_message(message: types.Message, state: FSMContext):
    """Принимает имя новой заметки"""
    global d
    d[message.text] = ''
    global name_of_new_note
    global notes_buttons
    f = True
    g = set()
    for i in range(len(notes_buttons)):
        g.add(notes_buttons[i].values['text'])
    if message.text in g:
        await message.answer('Такое имя заметки уже существует, выберите другое.')
    else:
        n = len(notes_buttons) - 2
        name_of_new_note = message.text
        new_button = InlineKeyboardButton(name_of_new_note, callback_data=f'Заметка {n}')
        notes_buttons.append(new_button)
        await state.set_state('value_of_new_note')
        await message.answer('Что хочешь записать в заметку?')


@dp.message_handler(state='value_of_new_note')
async def about_bot_message(message: types.Message, state: FSMContext):
    """Записывает заметку"""
    global d
    global last_content
    d[name_of_new_note] = message.text
    last_content = message.text
    await message.answer('Заметка записана!')
    await message.answer(**main_menu)


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
def count_slov(s):
    s = s + ' '
    angl = set('1234567890qwertyuiopasdfghjklzxcvbnm')
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

@dp.callback_query_handler(lambda c: c.data == f'Заметка 1', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[3].values['text']
    await call.message.answer(f'Имя: {name}')
    await call.message.answer(f'Содержание: {d[name]}')
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 2', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[4].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 3', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[5].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 4', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[6].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 5', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[7].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 6', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[8].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 7', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[9].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 8', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[10].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 9', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[11].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

@dp.callback_query_handler(lambda c: c.data == f'Заметка 10', state = '*')
async def about_bot_message(call: types.CallbackQuery, state: FSMContext):
    global notes_buttons
    global d
    global n
    name = notes_buttons[12].values['text']
    await call.message.answer(f'{name}:')
    await call.message.answer(d[name])
    await call.message.answer(f'Кол-во слов: {count_slov(d[name])}')

executor.start_polling(dp, skip_updates=True)
