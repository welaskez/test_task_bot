"""added name field to consultations table

Revision ID: f3fe46dcc20a
Revises: bdb481426e46
Create Date: 2025-02-20 13:09:28.782578

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f3fe46dcc20a"
down_revision: Union[str, None] = "bdb481426e46"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("consultations", sa.Column("name", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("consultations", "name")
