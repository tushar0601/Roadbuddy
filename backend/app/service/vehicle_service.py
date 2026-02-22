import uuid
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.vehicle_repository import VehicleRepository
from app.domain.vehicle.schema import VehicleCreate, VehicleOut
from app.domain.vehicle.model import Vehicle


class VehicleService:

    def __init__(self, db: Session):
        self.repo = VehicleRepository(db=db)

    def create_vehicle(self, payload: VehicleCreate, user_id: uuid.UUID) -> Vehicle:
        return self.repo.create_vehicle(payload=payload, user_id=user_id)

    def list_vehicles(self, user_id: uuid.UUID) -> List[Vehicle]:
        return self.repo.list_vehicles(user_id=user_id)

    def get_by_id(self, vehicle_id: uuid.UUID) -> Optional[Vehicle]:
        return self.repo.get_by_id(vehicle_id=vehicle_id)
