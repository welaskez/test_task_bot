from core.models import Response
from crud.response import ResponseCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class ResponseService(BaseService[Response]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, ResponseCRUD)
        self.crud: ResponseCRUD = self.crud
