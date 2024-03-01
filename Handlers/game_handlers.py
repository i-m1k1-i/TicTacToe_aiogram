import logging

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery  # noqa
from aiogram.fsm.context import FSMContext
from Filters.filters import IsHisTurn

from Keyboards.main_keyboards import getKb_3x3, getKb_cancel_searching, getKb_mainMenu
from Lexicon.lexicon import lexicon_ru
from Database.users import users, waiting_users
from FSM.state_groups import FSMGame
from constants import FREE, X, O
from Utils.utils import (does_win, get_deskMessageId, pair_users,
                         get_user_state, send_winner_messages, update_desk)


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
        user1.shape = X
        user2.shape = O
        user1.move = True
        user2.move = False

        user2_state = get_user_state(bot.id, user2.id, dispatcher)
        user2_stateData = await user2_state.get_data()
        user2_gameMessage = user2_stateData["deskMessage_id"]

        await callback.message.edit_text(f"Твой оппонент {user2.username}",
                                         reply_markup=getKb_3x3(user1.desk))
        await bot.edit_message_text(f"Твой оппонент {user1.username}",
                                    user2.id, user2_gameMessage,
                                    reply_markup=getKb_3x3(user2.desk))
        await state.set_state(FSMGame.inGame)
        await user2_state.set_state(FSMGame.inGame)

        logger.info("in if 1")
    else:
        waiting_users.append(callback.from_user.id)
        await callback.message.edit_text(
            lexicon_ru.searching_opponent,
            reply_markup=getKb_cancel_searching()
        )
        await state.set_state(FSMGame.searching)
        logger.info("else 1")

    await state.update_data(deskMessage_id=callback.message.message_id)


@router.callback_query(F.data == "cancel_searching")
async def cancel_connection(callback: CallbackQuery):
    waiting_users.remove(callback.from_user.id)
    await callback.message.answer(lexicon_ru.main_menu,
                                  reply_markup=getKb_mainMenu())


@router.callback_query(F.data.startswith("move"), IsHisTurn())
async def make_move(callback: CallbackQuery, bot: Bot, dispatcher: Dispatcher):
    user1 = users[callback.from_user.id]  # his turn
    user2 = users[user1.opponent]
    user2_deskMessageId = await get_deskMessageId(bot, dispatcher, user2.id)
    move_pos = int(callback.data.split('_')[1])

    if user1.desk[move_pos] == FREE:
        user1.desk[move_pos] = user1.shape
        user2.desk[move_pos] = user1.shape
        await update_desk(callback, bot, user2.id, user2_deskMessageId, user1.desk, user1.shape)
        await callback.answer()
    else:
        await callback.answer("This cell is occupied")

    winner = does_win(user1, user2, user1.desk)
    if winner:
        await send_winner_messages(user1, user2, winner, bot,
                                   callback.message.message_id, user2_deskMessageId)

    user1.move, user2.move = user2.move, user1.move


@router.callback_query(F.data.startswith("move"))
async def make_move_notOnHisMove(callback: CallbackQuery):
    await callback.answer("Сейчас не твой ход")
