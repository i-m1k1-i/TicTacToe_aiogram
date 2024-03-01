import logging
from Database.users import users, waiting_users, User
from Keyboards.main_keyboards import getKb_3x3, getKb_mainMenu
from constants import WIN_COMBINATIONS, X, O

from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey


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


def pair_users(id1: int, id2: int):
    user1 = users[id1]
    user2 = users[id2]
    waiting_users.remove(id2)

    user1.opponent = user2.id
    user2.opponent = user1.id

    users[user1.id] = user1
    users[user2.id] = user2
    return user1, user2


def does_win(user1: User, user2: User, desk: list[int]):
    for c in WIN_COMBINATIONS:
        if desk[c[0]] in (X, O) and desk[c[0]] == desk[c[1]] == desk[c[2]]:
            return user1 if user1.shape == desk[c[0]] else user2
    return None


def get_user_state(botId: int, userId: int, dp: Dispatcher) -> FSMContext:
    new_user_storage_key = StorageKey(botId, userId, userId)
    context = FSMContext(storage=dp.storage, key=new_user_storage_key)
    return context


async def get_deskMessageId(bot: Bot, dispatcher: Dispatcher, user_id: int) -> int:
    user2_state = get_user_state(bot.id, user_id, dispatcher)
    user2_stateData = await user2_state.get_data()
    return user2_stateData["deskMessage_id"]


async def send_winner_messages(user1: User, user2: User, winner: User,
                               bot: Bot, message1: int, message2: int):
    looser = user1 if winner == user2 else user2
    if winner == user2:
        message1, message2 = message2, message1

    await bot.edit_message_text("Поздравляю, Вы победили!",
                                winner.id,
                                message1,
                                reply_markup=getKb_mainMenu())
    await bot.edit_message_text("К сожелению вы проиграли, повезет в следующий раз.",
                                looser.id,
                                message2,
                                reply_markup=getKb_mainMenu())
