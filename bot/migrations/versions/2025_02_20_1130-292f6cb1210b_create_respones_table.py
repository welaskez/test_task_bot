"""create respones table

Revision ID: 292f6cb1210b
Revises: fcb797e9064c
Create Date: 2025-02-20 11:30:21.825699

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "292f6cb1210b"
down_revision: Union[str, None] = "fcb797e9064c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "responses",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("type", sa.Enum("TAROT", "FINANCE", name="responseenum"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_responses")),
    )


def downgrade() -> None:
    op.drop_table("responses")
