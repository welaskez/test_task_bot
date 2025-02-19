from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class User(UuidPkMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
