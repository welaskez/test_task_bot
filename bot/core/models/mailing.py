from datetime import datetime

from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Mailing(UuidPkMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    time: Mapped[datetime]
    text: Mapped[str]
