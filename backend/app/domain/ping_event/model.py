import uuid
from enum import Enum
from sqlalchemy import String, DateTime, func, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class PingReason(str, Enum):
    BLOCKED = "BLOCKED"
    WRONG_PARKING = "WRONG_PARKING"
    EMERGENCY = "EMERGENCY"


class PingEvent(Base):
    __tablename__ = "ping_events"
    __table_args__ = {"schema": "ping"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    sticker_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("sticker.stickers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    reason: Mapped[str] = mapped_column(String(32), nullable=False)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)

    ip_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(256), nullable=True)

    created_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True, nullable=False
    )
