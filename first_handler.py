from aiogram import Bot
from aiogram.types import Message

async def start_handle(msg: Message, bot: Bot):
    await msg.answer(text = "Hello! I am your fucking bot")

async def help_handle(msg: Message, bot: Bot):
    await msg.answer(text = "WHAT DO YOU WANT?")

async def cancel_handle(msg: Message, bot: Bot):
    await msg.answer(text = "Goodbye")

#chat_id=msg.from_user.id,
async def hi_handle(msg: Message, bot: Bot):
    await msg.answer(text = f'Привет {msg.from_user.first_name}')

async def photo_handle(msg: Message, bot: Bot):
    await msg.reply('Крутое фото')

async def errow_handle(msg: Message, bot: Bot):
    await msg.answer(text = f'Я не хочу с тобой говорить {msg.from_user.first_name}')
