from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_race():
    key = InlineKeyboardBuilder()
    key.button(text = 'Гоблин', callback_data='гоблин')
    key.button(text = 'Драугр', callback_data='драугр')
    key.button(text = 'Орк', callback_data='орк')
    key.button(text = 'Гомункул', callback_data='гомункул')
    return key.as_markup()

def get_inline_class():
    key = InlineKeyboardBuilder()
    key.button(text = 'Тяжеловес', callback_data='тяжеловес')
    key.button(text = 'Стрелок', callback_data='стрелок')
    key.button(text = 'Потрошитель', callback_data='потрошитель')
    key.button(text = 'Некромант', callback_data='некромант')
    return key.as_markup()