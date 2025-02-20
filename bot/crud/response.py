from core.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class ResponseCRUD(BaseCRUD[Response]):
    model = Response

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
