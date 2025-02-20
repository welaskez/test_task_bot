from core.models import Consultation
from crud.consultation import ConsultationCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ConsultationService(BaseService[Consultation]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ConsultationCRUD)
        self.crud: ConsultationCRUD = self.crud
