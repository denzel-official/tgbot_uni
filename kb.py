from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Обменять", callback_data="exchange")],
    [InlineKeyboardButton(text="Пополнить баланс", callback_data="deposit"),
     InlineKeyboardButton(text="Проверить баланс", callback_data="balance")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

buy = [[InlineKeyboardButton(text='✅', pay=True),
        InlineKeyboardButton(text="⬅️", callback_data="buyrr"),
        InlineKeyboardButton(text="➡️", callback_data="buyee")]]

buy = InlineKeyboardMarkup(inline_keyboard=buy)
