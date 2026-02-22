from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class NotifyOwnerIn(BaseModel):
    message: str = "Please move your vehicle."


class NotificationOut(BaseModel):
    id: UUID
    vehicle_id: UUID
    title: str
    body: str
    data: dict
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
