"""create stickers and ping_events tables

Revision ID: 3ea59ae7f4e0
Revises: 95e4d7f0b6f3
Create Date: 2026-02-18 00:28:05.320721

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "3ea59ae7f4e0"
down_revision: Union[str, None] = "95e4d7f0b6f3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "stickers",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False
        ),
        sa.Column("vehicle_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("public_code", sa.String(length=64), nullable=False),
        sa.Column(
            "status",
            sa.String(length=16),
            nullable=False,
            server_default=sa.text("'ACTIVE'"),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["vehicle_id"], ["vehicle.vehicles.id"], ondelete="CASCADE"
        ),
        schema="sticker",
    )
    op.create_index(
        "ix_sticker_stickers_vehicle_id", "stickers", ["vehicle_id"], schema="sticker"
    )
    op.create_index(
        "ix_sticker_stickers_public_code",
        "stickers",
        ["public_code"],
        unique=True,
        schema="sticker",
    )

    op.create_table(
        "ping_events",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False
        ),
        sa.Column("sticker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("reason", sa.String(length=32), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("ip_hash", sa.String(length=64), nullable=True),
        sa.Column("user_agent", sa.String(length=256), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["sticker_id"], ["sticker.stickers.id"], ondelete="CASCADE"
        ),
        schema="ping",
    )
    op.create_index(
        "ix_ping_ping_events_sticker_id", "ping_events", ["sticker_id"], schema="ping"
    )
    op.create_index(
        "ix_ping_ping_events_created_at", "ping_events", ["created_at"], schema="ping"
    )


def downgrade() -> None:
    op.drop_index(
        "ix_ping_ping_events_created_at", table_name="ping_events", schema="ping"
    )
    op.drop_index(
        "ix_ping_ping_events_sticker_id", table_name="ping_events", schema="ping"
    )
    op.drop_table("ping_events", schema="ping")

    op.drop_index(
        "ix_sticker_stickers_public_code", table_name="stickers", schema="sticker"
    )
    op.drop_index(
        "ix_sticker_stickers_vehicle_id", table_name="stickers", schema="sticker"
    )
    op.drop_table("stickers", schema="sticker")
