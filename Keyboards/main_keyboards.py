import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from constants import EMOJIS, FREE
from Lexicon.lexicon import menu


logger = logging.getLogger(__name__)


def getKb_mainMenu():
    btns = [InlineKeyboardButton(text=text, callback_data=data)
            for text, data in menu]
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=2)
    return builder.as_markup()


def getKb_profile():
    btns = [InlineKeyboardButton(text=text, callback_data=data)
            for text, data in menu[0:1]]
    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=2)
    return builder.as_markup()


def getKb_3x3(user_desk_data: list, shape: int = FREE):
    btns = [InlineKeyboardButton(text=EMOJIS[cell_data], callback_data="move_" + str(cell_pos))
            for cell_pos, cell_data in enumerate(user_desk_data)]

    builder = InlineKeyboardBuilder()
    builder.row(*btns, width=3)
    return builder.as_markup()


def getKb_cancel_searching():
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Отменить",
                                               callback_data="cancel_searching")]])
