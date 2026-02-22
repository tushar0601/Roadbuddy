import uuid
import secrets
from enum import Enum

from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class StickerStatus(str, Enum):
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"


def generate_public_code() -> str:
    return secrets.token_urlsafe(16)


class Sticker(Base):
    __tablename__ = "stickers"
    __table_args__ = {"schema": "sticker"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    vehicle_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vehicle.vehicles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    public_code: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
        nullable=False,
        default=generate_public_code,
    )

    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default=StickerStatus.ACTIVE.value
    )

    created_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
