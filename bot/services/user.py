import message_texts
from aiogram.types import Message
from core.models import User
from core.schemas.user import UserCreate
from crud.user import UserCRUD
from keyboards.inline import common
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class UserService(BaseService[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserCRUD)
        self.crud: UserCRUD = self.crud

    async def get_by_tg_id(self, tg_id: int) -> User | None:
        return await self.crud.get_one_by_expression(User.tg_id == tg_id)

    async def handle_start(self, message: Message) -> None:
        user = await self.get_by_tg_id(message.from_user.id)
        if not user:
            await self.create(UserCreate(tg_id=message.from_user.id))

        await message.answer(text=message_texts.START, reply_markup=common.start_kb)
