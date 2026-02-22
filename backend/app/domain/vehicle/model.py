import uuid
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base


class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = {"schema": "vehicle"}
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("app_user.users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    label: Mapped[str] = mapped_column(String(80), nullable=False) 
    plate_last4: Mapped[str | None] = mapped_column(String(4), nullable=True)

    created_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

