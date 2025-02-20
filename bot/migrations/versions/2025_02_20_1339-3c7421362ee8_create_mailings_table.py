"""create mailings table

Revision ID: 3c7421362ee8
Revises: f3fe46dcc20a
Create Date: 2025-02-20 13:39:28.956281

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3c7421362ee8"
down_revision: Union[str, None] = "f3fe46dcc20a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "mailings",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("time", sa.DateTime(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("status", sa.Enum("PENDING", "SENT", name="mailingstatus"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_mailings")),
    )


def downgrade() -> None:
    op.drop_table("mailings")
