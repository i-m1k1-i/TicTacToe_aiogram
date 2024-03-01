from aiogram.types import CallbackQuery
from aiogram.filters import BaseFilter

from Database.users import users


class IsHisTurn(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return users[callback.from_user.id].move
