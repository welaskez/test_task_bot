from core.models import Mailing
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class MailingCRUD(BaseCRUD[Mailing]):
    model = Mailing

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
