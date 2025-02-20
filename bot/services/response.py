from aiogram.types import CallbackQuery
from core.enums import ResponseEnum
from core.models import Response
from crud.response import ResponseCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ResponseService(BaseService[Response]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ResponseCRUD)
        self.crud: ResponseCRUD = self.crud

    async def get_random_response_text(self, response_type: ResponseEnum) -> str:
        response = await self.crud.get_random_response(response_type)
        return response.text

    async def handle_tarot(self, callback: CallbackQuery) -> None:
        await callback.message.answer(text="🔮 Перемешиваю карты...")
        text = await self.get_random_response_text(ResponseEnum.TAROT)
        await callback.message.answer(text)
        await callback.answer()
