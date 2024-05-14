from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from choose import PlayerRegistrationState as PRS
from chooseDop import get_inline_race, get_inline_class
import json
import os

async def get_form_handler(msg: Message, state: FSMContext):
    await msg.answer('Добро пожаловать в игру')
    await state.set_state(PRS.hero_name)

async def get_name_handler(msg: Message, state: FSMContext):
    await msg.answer(f'Ваше имя {msg.text}.',reply_markup=get_inline_race())
    await state.update_data(hero_name = msg.text)
    await state.set_state(PRS.hero_race)

async def get_race_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Ваша раса {call.data}.',reply_markup=get_inline_class())
    await state.update_data(hero_race = call.data)
    await state.set_state(PRS.hero_class)
    await call.answer()

async def get_class_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Загрузите фото')
    await state.update_data(hero_class = call.data)
    await state.set_state(PRS.hero_avatar)
    await call.answer()

async def get_avatar_handler(msg: Message, state: FSMContext):
    try:
        file = msg.photo[-1].file_id
        await state.update_data(hero_avatar = file)
        data = await state.get_data()
        our_dir = os.getcwd()
        #file_name = str(msg.from_user.id) + '.json'
        #file_path = os.path.join(our_dir, 'db/characters', file_name)
        #with open(file_path, 'w',encoding = 'utf-8') as f:
            #json.dump(data,f, ensure_ascii = False)
        await msg.answer_photo(photo = file, caption = f'Поздравляю вами создан {data["hero_race"]} {data["hero_class"]} по имени {data["hero_name"]}')
        await state.clear()
    except:
        await msg.answer('Ошибка. Фото нет.')

#async def get_character_handler(msg: Message):
    #try:
        #our_dir = os.getcwd()
        #file_name = str(msg.from_user.id) + '.json'
        #file_path = os.path.join(our_dir, 'db/characters', file_name)
        #with open(file_path, 'r',encoding = 'utf-8') as f:
            #data = json.load(f)
            #await msg.answer_photo(photo = data['hero_avatar'], caption = f'Поздравляю вами создан {data["hero_race"]} {data["hero_class"]} по имени {data["hero_name"]}')
    #except:
        #await msg.answer('НЕТ ПЕРСОНАЖА')


                                                                                                                                                                          