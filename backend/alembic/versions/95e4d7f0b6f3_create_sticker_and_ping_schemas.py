"""create sticker and ping schemas

Revision ID: 95e4d7f0b6f3
Revises: d01fc010552f
Create Date: 2026-02-18 00:26:25.742032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95e4d7f0b6f3'
down_revision: Union[str, None] = 'd01fc010552f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS sticker")
    op.execute("CREATE SCHEMA IF NOT EXISTS ping")

def downgrade() -> None:
    op.execute("DROP SCHEMA IF EXISTS ping CASCADE")
    op.execute("DROP SCHEMA IF EXISTS sticker CASCADE")