from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove
menu_0 = [
    [InlineKeyboardButton(text="Exchange", callback_data="0_exchange"),
     InlineKeyboardButton(text="Upload", callback_data="0_upload")],
]
menu_0 = InlineKeyboardMarkup(inline_keyboard=menu_0)


menu_1 = [
    [InlineKeyboardButton(text="Tech", callback_data="1_tech"),
     InlineKeyboardButton(text="Cloth", callback_data="1_cloth")],
]
menu_1 = InlineKeyboardMarkup(inline_keyboard=menu_1)

menu_2 = [
    [InlineKeyboardButton(text="Upper", callback_data="2_upper", )],
    [InlineKeyboardButton(text="Lower", callback_data="2_lower")],
]
menu_2 = InlineKeyboardMarkup(inline_keyboard=menu_2)

menu_3 = [
    [InlineKeyboardButton(text="Hat", callback_data="3_Hat")],
    [InlineKeyboardButton(text="Torso", callback_data="3_torso")],
    [InlineKeyboardButton(text="Legs", callback_data="3_legs")],
    [InlineKeyboardButton(text="Feet", callback_data="3_feet")],
]
menu_3 = InlineKeyboardMarkup(inline_keyboard=menu_3)

menu_4 = [
    [InlineKeyboardButton(text="Red", callback_data="4_Red")],
    [InlineKeyboardButton(text="Black", callback_data="4_black")],
    [InlineKeyboardButton(text="White", callback_data="4_white")],
    [InlineKeyboardButton(text="Blue", callback_data="4_Blue")],
]
menu_4 = InlineKeyboardMarkup(inline_keyboard=menu_4)

menu_5 = [
    [InlineKeyboardButton(text="1/5", callback_data="5_c_1")],
    [InlineKeyboardButton(text="2/5", callback_data="5_c_2")],
    [InlineKeyboardButton(text="3/5", callback_data="5_c_3")],
    [InlineKeyboardButton(text="4/5", callback_data="5_c_4")],
    [InlineKeyboardButton(text="5/5", callback_data="5_c_5")],
]
menu_5 = InlineKeyboardMarkup(inline_keyboard=menu_5)

menu_6 = [
    [InlineKeyboardButton(text="Next", callback_data="5_next")],
    [InlineKeyboardButton(text="Prev", callback_data="5_prev")],
]
menu_6 = InlineKeyboardMarkup(inline_keyboard=menu_6)
