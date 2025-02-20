import message_texts
from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from keyboards.inline import common
from services.consultation import ConsultationService
from services.user import UserService
from states.consultation import ConsultationState

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, user_service: UserService):
    await user_service.handle_start(message)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text=message_texts.HELP)


@router.message(ConsultationState.name, F.text)
async def handle_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ConsultationState.time)
    await message.answer(text="Введите желаемое время")


@router.message(ConsultationState.time, F.text)
async def handle_time(message: types.Message, state: FSMContext, consultation_service: ConsultationService):
    await consultation_service.add_consultation(message, state)


@router.message()
async def handle_message(message: types.Message):
    await message.answer(text=message_texts.START, reply_markup=common.start_kb)
