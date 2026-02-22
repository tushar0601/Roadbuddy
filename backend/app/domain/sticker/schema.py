from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class StickerOut(BaseModel):
    id: UUID
    vehicle_id: UUID
    public_code: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
