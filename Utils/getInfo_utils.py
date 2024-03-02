from aiogram import Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey


def get_user_state(botId: int, userId: int, dp: Dispatcher) -> FSMContext:
    new_user_storage_key = StorageKey(botId, userId, userId)
    context = FSMContext(storage=dp.storage, key=new_user_storage_key)
    return context


async def get_deskMessageId(bot: Bot, dispatcher: Dispatcher, user_id: int) -> int:
    user2_state = get_user_state(bot.id, user_id, dispatcher)
    user2_stateData = await user2_state.get_data()
    return user2_stateData["deskMessage_id"]
