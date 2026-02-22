"""create schemas user vehicle notification

Revision ID: 247d92f49f4e
Revises: 
Create Date: 2026-02-15 00:34:23.549576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '247d92f49f4e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS app_user")
    op.execute("CREATE SCHEMA IF NOT EXISTS vehicle")
    op.execute("CREATE SCHEMA IF NOT EXISTS notification")

def downgrade() -> None:
    # Drop in reverse order (safe)
    op.execute("DROP SCHEMA IF EXISTS notification CASCADE")
    op.execute("DROP SCHEMA IF EXISTS vehicle CASCADE")
    op.execute("DROP SCHEMA IF EXISTS app_user CASCADE")