from aiogram.fsm.state import StatesGroup, State


class FSMGame(StatesGroup):
    searching = State()
    inGame = State()
