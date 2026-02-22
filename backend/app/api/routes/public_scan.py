import hashlib
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.domain.ping_event.schema import PingIn
from app.domain.sticker.model import StickerStatus
from app.domain.notification.model import Notification
from app.api.deps import (
    get_sticker_service,
    get_vehicle_service,
    get_ping_service,
    get_notification_service,
)
from app.service.notification_service import NotificationService
from app.service.ping_service import PingService
from app.service.sticker_service import StickerService
from app.service.vehicle_service import VehicleService

router = APIRouter(prefix="/s", tags=["public"])


def hash_ip(ip: str) -> str:
    return hashlib.sha256(ip.encode("utf-8")).hexdigest()


@router.post("/{public_code}/ping")
def ping_owner(
    public_code: str,
    payload: PingIn,
    request: Request,
    sticker_service: StickerService = Depends(get_sticker_service),
    vehicle_service: VehicleService = Depends(get_vehicle_service),
    ping_service: PingService = Depends(get_ping_service),
    notification_service: NotificationService = Depends(get_notification_service),
):
    sticker = sticker_service.get_by_public_code(public_code=public_code)
    if not sticker or sticker.status != StickerStatus.ACTIVE.value:
        raise HTTPException(status_code=404, detail="Sticker not found")

    vehicle = vehicle_service.get_by_id(vehicle_id=sticker.vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    ip = request.client.host if request.client else ""
    ua = request.headers.get("user-agent")

    pe = ping_service.create_ping_event(
        payload=payload, sticker_id=sticker.id, ip_hash=hash_ip(ip=ip), ua=ua
    )

    data = Notification(
        user_id=vehicle.owner_id,
        vehicle_id=vehicle.id,
        type="VEHICLE_PING",
        title="Someone is requesting you to move your vehicle",
        body=f"Reason: {payload.reason}"
        + (f" — {payload.note}" if payload.note else ""),
        data={"sticker_id": str(sticker.id), "ping_event": True},
    )
    n = notification_service.create_notification(data=data)
    return {"ok": True}
