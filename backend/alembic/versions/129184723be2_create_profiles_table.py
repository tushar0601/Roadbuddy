"""create profiles table

Revision ID: 129184723be2
Revises: 6012a50471bb
Create Date: 2026-02-19 17:22:10.321576

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "129184723be2"
down_revision: Union[str, None] = "6012a50471bb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "profiles",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False
        ),
        sa.Column("supabase_user_id", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False, server_default=""),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        schema="app_user",  # <-- THIS is critical
    )

    op.create_index(
        "ix_app_user_profiles_supabase_user_id",
        "profiles",
        ["supabase_user_id"],
        unique=True,
        schema="app_user",
    )


def downgrade():
    op.drop_index(
        "ix_app_user_profiles_supabase_user_id",
        table_name="profiles",
        schema="app_user",
    )

    op.drop_table("profiles", schema="app_user")
