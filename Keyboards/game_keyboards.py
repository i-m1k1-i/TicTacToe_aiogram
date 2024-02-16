from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from constants import EMOJIS


"""user_desk_data = [1, 2, 0,
                     2, 1, 0,
                     2, 1, 0]"""


def getKb_3x3(user_desk_data: list):
    btns = [InlineKeyboardButton(text=EMOJIS[data], callback_data=str(data))
            for data in user_desk_data]
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=3)
    return builder.as_markup()
