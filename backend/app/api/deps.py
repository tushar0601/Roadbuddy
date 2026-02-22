from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core.config import settings
from app.core.security import decode_token
from app.domain.user.model import User
from app.service.user_service import UserService
from app.service.vehicle_service import VehicleService
from app.service.notification_service import NotificationService
from app.service.sticker_service import StickerService
from app.service.ping_service import PingService
from app.core.supabase_auth import verify_supabase_jwt
from app.repository.profile_repository import ProfileRepository

bearer = HTTPBearer(auto_error=False)


def get_ping_service(db: Session = Depends(get_db)) -> PingService:
    return PingService(db=db)


def get_sticker_service(db: Session = Depends(get_db)) -> StickerService:
    return StickerService(db=db)


def get_notification_service(db: Session = Depends(get_db)) -> NotificationService:
    return NotificationService(db=db)


def get_vehicle_service(db: Session = Depends(get_db)) -> VehicleService:
    return VehicleService(db=db)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db=db)


bearer = HTTPBearer(auto_error=False)


def get_current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
    db: Session = Depends(get_db),
):
    if creds is None or not creds.credentials:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        claims = verify_supabase_jwt(creds.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    profile_repo = ProfileRepository(db=db)
    profile = profile_repo.get_or_create_profile(
        supabase_user_id=claims.sub,
        email=claims.email,
    )

    return profile
