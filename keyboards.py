from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup



keyboard_markup = InlineKeyboardMarkup()
notes = InlineKeyboardButton('Заметки', callback_data='notes')
link_library = InlineKeyboardButton('Библиотека ссылок', callback_data='link_library')
keyboard_markup.row(notes, link_library)
button_back = InlineKeyboardButton("Вернуться назад", callback_data='back')
back_keyboard = InlineKeyboardMarkup().add(button_back)
add_button = InlineKeyboardButton("Добавить новую заметку", callback_data='add_note')
notes_keyboard = InlineKeyboardMarkup()
change_name = InlineKeyboardButton("Изменить имя", callback_data='change_name')
change_content = InlineKeyboardButton("Изменить содержимое", callback_data='change_content')
read_content = InlineKeyboardButton("Прочитать заметку", callback_data='read_content')
change_keyboard = InlineKeyboardMarkup().add(change_name).add(change_content).add(read_content)