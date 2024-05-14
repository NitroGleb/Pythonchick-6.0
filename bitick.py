from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from first_handler import start_handle, help_handle, cancel_handle, hi_handle, photo_handle, errow_handle
from commands import set_commands
from second_handler import  on_handle, off_handle, sleeping_handle, sleepy_handle
from chooseDop import *
from game import *
from choose import WorkState, PlayerRegistrationState as PRS
import asyncio

TOKEN = '6898982955:AAFp-nCwNwilyu0vRA6x12-BSJI4PSyPm7M'

async def start():
    bot = Bot(token = TOKEN)
    dp = Dispatcher()

    dp.startup.register(set_commands)

    dp.message.register(sleeping_handle, WorkState.OFF, Command(commands='on'))
    dp.message.register(sleepy_handle, WorkState.OFF)
    dp.message.register(off_handle, Command(commands='off'))
    dp.message.register(on_handle, WorkState.ON)
    #dp.message.register(get_inline_race)
    #dp.message.register(get_inline_class)
    dp.message.register(get_form_handler,Command(commands=['form']))
    dp.message.register(get_name_handler, PRS.hero_name)
    dp.callback_query.register(get_race_handler, PRS.hero_race)
    dp.callback_query.register(get_class_handler, PRS.hero_class)
    dp.message.register(get_avatar_handler, PRS.hero_avatar)
    #dp.message.register(get_character_handler)
    dp.message.register(start_handle, Command(commands=['start']))
    dp.message.register(help_handle, Command(commands=['help']))
    dp.message.register(cancel_handle, Command(commands=['cancel']))
    dp.message.register(hi_handle, F.text == 'Привет')
    dp.message.register(photo_handle, F.photo)
    dp.message.register(errow_handle)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())