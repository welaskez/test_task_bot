from core.models import Consultation
from crud.mailing import MailingCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class MailingService(BaseService[Consultation]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, MailingCRUD)
        self.crud: MailingCRUD = self.crud
