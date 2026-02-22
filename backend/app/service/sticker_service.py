import uuid
from typing import Optional, List
from sqlalchemy.orm import Session
from app.repository.sticker_repository import StickerRepository
from app.domain.sticker.model import Sticker, StickerStatus


class StickerService:

    def __init__(self, db: Session):
        self.repo = StickerRepository(db=db)

    def create_sticker(
        self, vehicle_id: uuid.UUID, status: str
    ) -> Sticker:
        return self.repo.create_sticker(vehicle_id=vehicle_id, status=status)

    def get_by_public_code(self, public_code: str) -> Optional[Sticker]:
        return self.repo.get_by_public_code(public_code=public_code)

    def get_by_vehicle_id(self, vehicle_id: uuid.UUID) -> Optional[Sticker]:
        return self.repo.get_by_vehicle_id(vehicle_id=vehicle_id)
