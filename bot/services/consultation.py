from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.models import Consultation
from core.schemas.consultation import ConsultationCreate
from crud.consultation import ConsultationCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ConsultationService(BaseService[Consultation]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ConsultationCRUD)
        self.crud: ConsultationCRUD = self.crud

    async def add_consultation(self, message: Message, state: FSMContext) -> None:
        await state.update_data(time=message.text)
        data = await state.get_data()
        await state.clear()

        await self.create(
            ConsultationCreate(
                name=data.get("name"),
                username=f"@{message.from_user.username}",
                time=data.get("time"),
            )
        )

        await message.answer("Заявка создана, пожалуйста ожидайте, вам напишут")
