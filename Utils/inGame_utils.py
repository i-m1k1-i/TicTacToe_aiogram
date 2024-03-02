import logging
from Database.users import User
from Keyboards.main_keyboards import getKb_3x3, getKb_mainMenu
from constants import WIN_COMBINATIONS, X, O, FREE
from Lexicon.lexicon import lexicon_ru

from aiogram import Bot
from aiogram.types import CallbackQuery


logger = logging.getLogger(__name__)


async def update_desk(callback_user1: CallbackQuery, bot: Bot,
                      user2_id: int, user2_deskMessage,
                      desk: list[int], shape: int):
    await callback_user1.message.edit_reply_markup(
        reply_markup=getKb_3x3(desk, shape))
    await bot.edit_message_reply_markup(user2_id,
                                        user2_deskMessage,
                                        reply_markup=getKb_3x3(desk, shape)
                                        )


def does_win(user1: User, user2: User, desk: list[int]):
    for c in WIN_COMBINATIONS:
        if desk[c[0]] in (X, O) and desk[c[0]] == desk[c[1]] == desk[c[2]]:
            return user1 if user1.shape == desk[c[0]] else user2
    if FREE not in desk:
        return 'T'
    return None


async def send_winner_messages(user1: User, user2: User, winner: User,
                               bot: Bot, message1: int, message2: int):
    looser = user1 if winner == user2 else user2
    if winner == user2:
        message1, message2 = message2, message1

    await bot.edit_message_text(lexicon_ru.you_win,
                                winner.id,
                                message1,
                                reply_markup=getKb_mainMenu())
    await bot.edit_message_text(lexicon_ru.you_lose,
                                looser.id,
                                message2,
                                reply_markup=getKb_mainMenu())


async def send_tie_messages(user1: User, user2: User, bot: Bot,
                            message1: int, message2: int):
    await bot.edit_message_text(lexicon_ru.its_tie,
                                user1.id,
                                message1,
                                reply_markup=getKb_mainMenu())
    await bot.edit_message_text(lexicon_ru.its_tie,
                                user2.id,
                                message2,
                                reply_markup=getKb_mainMenu())
