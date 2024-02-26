from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from constants import EMOJIS
from Lexicon.lexicon import menu

"""user_desk_data = [1, 2, 0,
                     2, 1, 0,
                     2, 1, 0]"""


def getKb_mainMenu():
    btns = [InlineKeyboardButton(text=text, callback_data=data)
            for text, data in menu]
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=2)
    return builder.as_markup()


def getKb_3x3(user_desk_data: list):
    btns = [InlineKeyboardButton(text=EMOJIS[desk_data], callback_data=str(desk_pos))
            for desk_data, desk_pos in zip(user_desk_data, range(9))]
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=3)
    return builder.as_markup()
