from pydantic import BaseModel
from uuid import UUID


class VehicleCreate(BaseModel):
    label: str
    plate_last4: str | None = None


class VehicleOut(BaseModel):
    id: UUID
    label: str
    plate_last4: str | None

    class Config:
        from_attributes = True
