from core.enums import ResponseEnum
from core.models import Response
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD


class ResponseCRUD(BaseCRUD[Response]):
    model = Response

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_random_response(self, response_type: ResponseEnum) -> Response:
        stmt = select(Response).where(Response.type == response_type).order_by(func.random()).limit(1)
        return await self.session.scalar(stmt)
