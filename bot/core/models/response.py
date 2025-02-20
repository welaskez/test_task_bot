from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from core.enums.response import ResponseEnum

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Response(UuidPkMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    text: Mapped[str]
    type: Mapped[ResponseEnum] = mapped_column(Enum(ResponseEnum))
