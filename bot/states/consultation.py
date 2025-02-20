from aiogram.fsm.state import State, StatesGroup


class ConsultationState(StatesGroup):
    name = State()
    time = State()
