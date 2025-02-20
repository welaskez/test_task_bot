from datetime import datetime

from core.models import Mailing
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class MailingCRUD(BaseCRUD[Mailing]):
    model = Mailing

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_scheduled_mailings(self) -> list[Mailing]:
        stmt = select(Mailing).where(Mailing.time <= datetime.now())
        return list(await self.session.scalars(stmt))
