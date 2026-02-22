"""create users vehicles notifications tables

Revision ID: d01fc010552f
Revises: 247d92f49f4e
Create Date: 2026-02-15 00:45:12.954681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = 'd01fc010552f'
down_revision: Union[str, None] = '247d92f49f4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        schema="app_user",
    )

    op.create_index(
        "ix_app_user_users_email",
        "users",
        ["email"],
        unique=True,
        schema="app_user",
    )

    op.create_table(
        "vehicles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("owner_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("label", sa.String(length=80), nullable=False),
        sa.Column("plate_last4", sa.String(length=4), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["app_user.users.id"],
            ondelete="CASCADE",
        ),
        schema="vehicle",
    )

    op.create_index(
        "ix_vehicle_vehicles_owner_id",
        "vehicles",
        ["owner_id"],
        schema="vehicle",
    )

    op.create_table(
        "notifications",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("vehicle_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "type",
            sa.String(length=50),
            nullable=False,
            server_default=sa.text("'VEHICLE_PING'"),
        ),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column(
            "data",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column(
            "is_read",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["app_user.users.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["vehicle_id"],
            ["vehicle.vehicles.id"],
            ondelete="CASCADE",
        ),
        schema="notification",
    )

    op.create_index(
        "ix_notification_notifications_user_id",
        "notifications",
        ["user_id"],
        schema="notification",
    )
    op.create_index(
        "ix_notification_notifications_vehicle_id",
        "notifications",
        ["vehicle_id"],
        schema="notification",
    )
    op.create_index(
        "ix_notification_notifications_created_at",
        "notifications",
        ["created_at"],
        schema="notification",
    )


def downgrade() -> None:
    op.drop_index("ix_notification_notifications_created_at", table_name="notifications", schema="notification")
    op.drop_index("ix_notification_notifications_vehicle_id", table_name="notifications", schema="notification")
    op.drop_index("ix_notification_notifications_user_id", table_name="notifications", schema="notification")
    op.drop_table("notifications", schema="notification")

    op.drop_index("ix_vehicle_vehicles_owner_id", table_name="vehicles", schema="vehicle")
    op.drop_table("vehicles", schema="vehicle")

    op.drop_index("ix_app_user_users_email", table_name="users", schema="app_user")
    op.drop_table("users", schema="app_user")