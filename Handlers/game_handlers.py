from aiogram import Bot, Router, F  # noqa
from aiogram.types import Message, CallbackQuery  # noqa

from Lexicon.lexicon import lexicon_ru
from Database.users import waiting_users
from Utils.utils import pair_users


router = Router()


"""
Plan for connecting two random users

there is table "waiting_users", there is a column "pair" in "all_users" table
if there isn't user in waiting_users:
    we add the user to waiting_users
    and send message  text = "waiting for connection"
                      reply_markup = "cancel_connecting"
if there is user in waiting_users:
    we connect the user with last user in waiting_users
    and delete the last user from waiting_users in list

    send desk to user1
    send desk to user2

def get_user_database(userId: int):
    return user_data
"""


@router.callback_query(F.data == "playXO")
async def connect_players(callback: CallbackQuery, bot: Bot):
    if waiting_users:
        user1, user2 = pair_users(callback.from_user.id,
                                  waiting_users[0])
        await callback.message.edit_text(f"Твой оппонент {user2.username}")
        await bot.send_message(user2.id, f"Твой оппонент {user1.username}")

    else:
        waiting_users.append(callback.from_user.id)
        await callback.message.edit_text(lexicon_ru.searching_opponent)


@router.callback_query(F.data == "cancel_searching")
async def cancel_connection(callback: CallbackQuery):
    waiting_users.remove(callback.from_user.id)
    await callback.message.answer(lexicon_ru.main_menu)
