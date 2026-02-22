"""add supabase_user_id to users

Revision ID: 6012a50471bb
Revises: 3ea59ae7f4e0
Create Date: 2026-02-19 17:09:30.598944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6012a50471bb'
down_revision: Union[str, None] = '3ea59ae7f4e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("supabase_user_id", sa.String(), nullable=True),
        schema="app_user",
    )

    op.execute("""
        UPDATE app_user.users
        SET supabase_user_id = COALESCE(supabase_user_id, gen_random_uuid()::text)
        WHERE supabase_user_id IS NULL
    """)

    # 3) Set NOT NULL
    op.alter_column(
        "users",
        "supabase_user_id",
        nullable=False,
        schema="app_user",
    )

    op.create_unique_constraint(
        "uq_app_user_users_supabase_user_id",
        "users",
        ["supabase_user_id"],
        schema="app_user",
    )
    op.create_index(
        "ix_app_user_users_supabase_user_id",
        "users",
        ["supabase_user_id"],
        unique=True,  # optional; constraint already enforces uniqueness
        schema="app_user",
    )

    # 5) Make password_hash nullable
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=255),
        nullable=True,
        schema="app_user",
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=255),
        nullable=False,
        schema="app_user",
    )

    op.drop_index(
        "ix_app_user_users_supabase_user_id",
        table_name="users",
        schema="app_user",
    )
    op.drop_constraint(
        "uq_app_user_users_supabase_user_id",
        "users",
        type_="unique",
        schema="app_user",
    )
    op.drop_column("users", "supabase_user_id", schema="app_user")
