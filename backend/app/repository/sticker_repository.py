from typing import Optional, List
from sqlalchemy.orm import Session
import uuid
from app.domain.sticker.model import Sticker, StickerStatus


class StickerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_sticker(self, vehicle_id: uuid.UUID, status: str):
        s = Sticker(vehicle_id=vehicle_id, status=status)
        self.db.add(s)
        self.db.commit()
        self.db.refresh(s)
        return s

    def get_by_public_code(self, public_code: str) -> Optional[Sticker]:
        return self.db.query(Sticker).filter(Sticker.public_code == public_code).first()

    def get_by_vehicle_id(self, vehicle_id: uuid.UUID) -> Optional[Sticker]:
        return (
            self.db.query(Sticker)
            .filter(
                Sticker.vehicle_id == vehicle_id,
                Sticker.status == StickerStatus.ACTIVE.value,
            )
            .first()
        )
