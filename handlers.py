from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import *

import kb
import config

query = []
li = [
    ['https://yt3.googleusercontent.com/ytc/AIf8zZS5g_exHmPXTkUKTc1H0_YxFpjwoT_adnHsxNVq_Q=s176-c-k-c0x00ffffff-no-rj',
     '1',
     'Hat', 'Red', '3/5'],
    ['https://www.bigw.com.au/medias/sys_master/images/images/hd0/h21/33525216378910.jpg', '2', 'Hat', 'Red', '3/5'],
    [
        'https://media.istockphoto.com/id/185093700/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BB%D0%B5%D0%BF%D1%80%D0%B5%D0%BA%D0%BE%D0%BD-%D1%88%D0%BB%D1%8F%D0%BF%D0%B0.webp?s=2048x2048&w=is&k=20&c=rDeCDCXudORiR1wBT86fXPaFpYsiii9DvYrwJBwR3W4=',
        '3', 'Hat', 'Red', '3/5'], ]


def gg(l_q, l_all):
    e = []
    for i in l_all:
        if sorted(i[2::]) == sorted(l_q):
            e += [i]
    return e


router = Router()
i = -1


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer('Hi {name}!'.format(name=msg.from_user.full_name), reply_markup=kb.menu_0)


@router.callback_query()
async def choosing_type_1(call: CallbackQuery):
    global query, i
    if call.data == '0_exchange':
        await call.message.delete()
        await call.message.answer('Выберите type_1', reply_markup=kb.menu_1)
    if call.data.startswith('1'):
        await call.message.delete()
        await call.message.answer('Выберите type_2', reply_markup=kb.menu_2)
    if call.data.startswith('2'):
        await call.message.delete()
        await call.message.answer('Выберите type_3', reply_markup=kb.menu_3)
    if call.data.startswith('3'):
        await call.message.delete()
        query += [call.data.split('_')[-1]]
        await call.message.answer('Выберите type_2', reply_markup=kb.menu_4)
    if call.data.startswith('4'):
        await call.message.delete()
        query += [call.data.split('_')[-1]]
        await call.message.answer('Выберите type_2', reply_markup=kb.menu_5)
    if call.data.startswith('5'):
        await call.message.delete()
        if call.data.startswith('5_c'):
            query += [call.data.split('_')[-1] + '/5']
        e = gg(query, li)
        if call.data == '5_prev':
            i -= 1
        if call.data == '5_next':
            i += 1
        if i == len(e):
            i = 0
        await call.message.answer_photo(e[i][0], caption=e[i][1], reply_markup=kb.menu_6, )
