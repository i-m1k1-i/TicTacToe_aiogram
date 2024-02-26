import logging

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery  # noqa
from aiogram.fsm.context import FSMContext

from Keyboards.main_keyboards import getKb_3x3
from Lexicon.lexicon import lexicon_ru
from Database.users import users, waiting_users
from FSM.state_groups import FSMGame
from Utils.utils import pair_users, set_state_for

logger = logging.getLogger(__name__)
router = Router()


@router.callback_query(F.data == "playXO")
async def connect_players(callback: CallbackQuery, bot: Bot,
                          state: FSMContext, dispatcher: Dispatcher):
    if waiting_users:
        user1, user2 = pair_users(callback.from_user.id,
                                  waiting_users[0])
        user1.create_desk()
        user2.create_desk()

        await callback.message.edit_text(f"Твой оппонент {user2.username}",
                                         reply_markup=getKb_3x3(user1.desk))
        await bot.send_message(user2.id, f"Твой оппонент {user1.username}",
                               reply_markup=getKb_3x3(user2.desk))
        await state.set_state(FSMGame.inGame)
        await set_state_for(bot.id, user2.id, dispatcher)

        logger.info("in if 1")
    else:
        waiting_users.append(callback.from_user.id)
        await callback.message.edit_text(lexicon_ru.searching_opponent)
        await state.set_state(FSMGame.searching)

        logger.info("else 1")


@router.callback_query(F.data == "cancel_searching")
async def cancel_connection(callback: CallbackQuery):
    waiting_users.remove(callback.from_user.id)
    await callback.message.answer(lexicon_ru.main_menu)


@router.callback_query(F.data.startswith("move"))
async def make_move(callback: CallbackQuery):
    move_pos = callback.data.split('_')[1]
    user1 = users[callback.from_user.id]  # his move
    user2 = users[user1.opponent]

    if user1.desk[move_pos] == 0:
        user1.desk[move_pos] = user1.shape
        user2.desk[move_pos] = user2.shape
    else:
        await callback.answer("This cell is occupied")
