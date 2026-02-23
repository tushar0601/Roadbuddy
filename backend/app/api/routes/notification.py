from fastapi import APIRouter, Depends, HTTPException, Request
from app.api.deps import get_current_user, get_vehicle_service, get_notification_service
from app.domain.notification.model import Notification
from app.domain.notification.schema import NotificationOut, NotifyOwnerIn
from app.domain.vehicle.model import Vehicle
from app.service.notification_service import NotificationService
from app.service.vehicle_service import VehicleService
from app.domain.profile.model import Profile

router = APIRouter()


@router.post("/vehicle/{vehicle_id}", response_model=NotificationOut)
def notify_vehicle_owner(
    vehicle_id: str,
    payload: NotifyOwnerIn,
    request: Request,
    vehicle_service: VehicleService = Depends(get_vehicle_service),
    notification_service: NotificationService = Depends(get_notification_service),
):
    vehicle = vehicle_service.get_by_id(vehicle_id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    data = Notification(
        user_id=vehicle.owner_id,
        vehicle_id=vehicle.id,
        type="VEHICLE_PING",
        title="Someone is requesting you to move your vehicle",
        body=payload.message,
        data={
            "ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent"),
        },
    )
    output = notification_service.create_notification(data=data)
    return output


@router.get("/me", response_model=list[NotificationOut])
def get_my_notifications(
    notification_service: NotificationService = Depends(get_notification_service),
    profile: Profile = Depends(get_current_user),
):
    return notification_service.get_notifications(user_id=profile.id)
