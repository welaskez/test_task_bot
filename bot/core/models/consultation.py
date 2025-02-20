from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Consultation(UuidPkMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    username: Mapped[str]
    time: Mapped[str]
