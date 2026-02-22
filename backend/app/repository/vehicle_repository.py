from typing import List, Optional
import uuid
from sqlalchemy.orm import Session
from app.domain.vehicle.schema import VehicleCreate
from app.domain.vehicle.model import Vehicle


class VehicleRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, payload: VehicleCreate, user_id: uuid.UUID) -> Vehicle:
        v = Vehicle(
            owner_id=user_id, label=payload.label, plate_last4=payload.plate_last4
        )
        self.db.add(v)
        self.db.commit()
        self.db.refresh(v)
        return v

    def list_vehicles(self, user_id: uuid.UUID) -> List[Vehicle]:
        return (
            self.db.query(Vehicle)
            .filter(Vehicle.owner_id == user_id)
            .order_by(Vehicle.created_at.desc())
            .all()
        )

    def get_by_id(self, vehicle_id: uuid.UUID) -> Optional[Vehicle]:
        return self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
