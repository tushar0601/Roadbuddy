from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import (
    get_vehicle_service,
    get_sticker_service,
)
from app.domain.sticker.model import StickerStatus
from app.domain.sticker.schema import StickerOut
from app.service.sticker_service import StickerService
from app.service.vehicle_service import VehicleService

router = APIRouter(prefix="/vehicles", tags=["stickers"])


@router.post("/{vehicle_id}/stickers", response_model=StickerOut)
def create_sticker(
    vehicle_id: str,
    vehicle_service: VehicleService = Depends(get_vehicle_service),
    sticker_service: StickerService = Depends(get_sticker_service),
):
    v = vehicle_service.get_by_id(vehicle_id=vehicle_id)
    if not v:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    sticker = sticker_service.get_by_vehicle_id(vehicle_id=vehicle_id)
    if sticker:
        return sticker
    s = sticker_service.create_sticker(
        vehicle_id=vehicle_id, status=StickerStatus.ACTIVE.value
    )
    return s
