import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import Handlers as H
from Config.config import load_config


format = "%(levelname)s [%(filename)s/%(name)s: %(lineno)d]: |%(message)s|"


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=format)
    config = load_config()
    storage = MemoryStorage()

    bot = Bot(token=config.bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    dp.include_routers(H.info_handlers.router,
                       H.game_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
