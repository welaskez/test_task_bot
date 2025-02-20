"""create consultations table

Revision ID: bdb481426e46
Revises: 292f6cb1210b
Create Date: 2025-02-20 13:00:34.986183

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bdb481426e46"
down_revision: Union[str, None] = "292f6cb1210b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "consultations",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("time", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_consultations")),
    )


def downgrade() -> None:
    op.drop_table("consultations")
