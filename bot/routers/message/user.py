import message_texts
from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from keyboards.inline import common
from services.user import UserService

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, user_service: UserService):
    await user_service.handle_start(message)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text=message_texts.HELP)


@router.message()
async def handle_message(message: types.Message):
    await message.answer(text=message_texts.START, reply_markup=common.start_kb)
