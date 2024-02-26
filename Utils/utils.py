from Database.users import users, waiting_users, User
from constants import WIN_COMBINATIONS
from FSM.state_groups import FSMGame

from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey


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
        if desk[c[0]] == desk[c[1]] == desk[c[2]]:
            return user1 if user1.shape == desk[c[0]] else user2


async def set_state_for(botId: int, userId: int, dp: Dispatcher):
    new_user_storage_key = StorageKey(botId, userId, userId)
    context = FSMContext(storage=dp.storage, key=new_user_storage_key)
    await context.set_state(FSMGame.inGame)
    return 0
