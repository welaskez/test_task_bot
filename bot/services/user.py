from core.models import User
from crud.user import UserCRUD
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseService


class UserService(BaseService[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, UserCRUD)
        self.crud: UserCRUD = self.crud
