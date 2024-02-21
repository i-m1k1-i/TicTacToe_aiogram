from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from Lexicon.lexicon import lexicon_ru
from Database.users import users, User
from Keyboards.main_keyboards import getKb_mainMenu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = User(user_id, message.from_user.username)

    await message.answer(lexicon_ru.start,
                         reply_markup=getKb_mainMenu())
