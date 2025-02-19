from aiogram import Router, types
from aiogram.filters import CommandStart
from services.user import UserService

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, user_service: UserService):
    await user_service.handle_start(message)
