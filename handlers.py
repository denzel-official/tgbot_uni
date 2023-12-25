from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import *

import kb
import text
import config


class Choose(StatesGroup):
    choosing_good = State()


class Upload(StatesGroup):
    uploading_good = State()


router = Router()
lp = types.LabeledPrice(label='rup', amount=100000)
f = 0


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))


@router.message(Command("exchange"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer('Напишите что вас интересует')
    await state.set_state(Choose.choosing_good)


@router.message(Command("upload"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))


@router.message(F.text, Choose.choosing_good)
async def cmd_buy(msg: Message, state: FSMContext):
    # здесь нужно присвоить некоторый элемент бд, который соответствует поиску, переменной
    # поиск это message.text
    # дальше
    await msg.answer_photo(FSInputFile('Cat.jpg'), caption='Описание товара\nВладелец: @Baba3Yaga')
    await state.clear()
