from fastapi import APIRouter, Depends
from app.api.deps import get_vehicle_service, get_current_user
from app.domain.vehicle.schema import VehicleCreate, VehicleOut
from app.service.vehicle_service import VehicleService
from app.domain.user.model import User

router = APIRouter()


@router.post("", response_model=VehicleOut)
def create_vehicle(
    payload: VehicleCreate,
    service: VehicleService = Depends(get_vehicle_service),
    user: User = Depends(get_current_user),
):
    return service.create_vehicle(payload=payload, user_id=user.id)


@router.get("", response_model=list[VehicleOut])
def list_vehicles(
    service: VehicleService = Depends(get_vehicle_service),
    user: User = Depends(get_current_user),
):
    return service.list_vehicles(user_id=user.id)
