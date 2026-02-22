# app/domain/profile/models.py
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.core.db import Base


class Profile(Base):
    __tablename__ = "profiles"
    __table_args__ = {"schema": "app_user"}
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    supabase_user_id = Column(String, nullable=False, unique=True, index=True)

    email = Column(String, nullable=False, default="")

    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
