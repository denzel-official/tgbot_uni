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


class Form(StatesGroup):
    choosing_good = State()


router = Router()
lp = types.LabeledPrice(label='rup', amount=100000)
f = 0


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))


@router.message(Command("exchange"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer('Напишите что вас интересует')
    await state.set_state(Form.choosing_good)


@router.message(Command("upload"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))


@router.message(F.text, Form.choosing_good)
async def cmd_buy(msg: Message):
    #здесь нужно присвоить некоторый элемент бд, который соответствует поиску, переменной
    #поиск это message.text
    #дальше
    await msg.answer_photo(FSInputFile('Cat.jpg'), caption='Описание товара\nВладелец: @Baba3Yaga')

# @router.message(F.text == "Меню")
# @router.message(Command("menu"))
# @router.message(F.text == "Выйти в меню")
# @router.message(F.text == "◀️ Выйти в меню")
# async def menu(msg: Message):
#     await msg.answer(text.menu, reply_markup=kb.menu)
#
#
# @router.callback_query(F.data == "exchange")
# async def input_text_prompt(clbck: CallbackQuery):
#     await clbck.answer(text.buy, parse_mode='Markdown')
#     f = 1
#
#
# @router.message(F.text)
# async def cmd_buy(msg: Message):
#     if f:
#         await msg.answer_invoice(title='ABIBAS CAP',
#                                  description='The biggest cap you have ever seen!',
#                                  provider_token=config.BOT_PAYMENT_TEST,
#                                  currency='rub',
#                                  photo_url='https://myreact.ru/wp-content/uploads/2023/05/trefoil_baseball_cap_black_ec3603_01_standard.jpg',
#                                  photo_height=1024,  # !=0/None or picture won't be shown
#                                  photo_width=1024,
#                                  photo_size=1024,
#                                  is_flexible=True,  # True If you need to set up Shipping Fee
#                                  prices=[lp],
#                                  start_parameter='cap',
#                                  payload='cap coupon',
#                                  reply_markup=kb.buy)
