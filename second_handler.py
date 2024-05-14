from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from choose import WorkState

async def on_handle(msg: Message, state: FSMContext):
    await msg.answer("Bot is working! /off")
    await state.set_state(WorkState.ON)

async def off_handle(msg: Message, state: FSMContext):
    await msg.answer("Go fuck yourself! /on")
    await state.set_state(WorkState.OFF)

async def sleeping_handle(msg: Message, state: FSMContext):
    await msg.answer("Bot is working /off")

async def sleepy_handle(msg: Message, state: FSMContext):
    await msg.answer("Go fuck yourself! /on")