from core.models import Consultation
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class ConsultationCRUD(BaseCRUD[Consultation]):
    model = Consultation

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
