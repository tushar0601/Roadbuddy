from fastapi import APIRouter
from app.api.routes.auth import router as auth_router
from app.api.routes.notification import router as notification_router
from app.api.routes.vehicle import router as vehicle_router
from app.api.routes.sticker import router as sticker_router
from app.api.routes.public_scan import router as public_router

router = APIRouter()

router.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
router.include_router(
    router=notification_router, prefix="/notification", tags=["Notification"]
)
router.include_router(router=vehicle_router, prefix="/vehicles", tags=["Vehicle"])
router.include_router(router=sticker_router)
router.include_router(router=public_router)
