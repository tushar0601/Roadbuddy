from sqlalchemy.orm import Session
import uuid
from typing import Optional

from app.domain.ping_event.schema import PingIn
from app.domain.ping_event.model import PingEvent
from app.repository.ping_repository import PingEventRepository


class PingService:

    def __init__(self, db: Session):
        self.repo = PingEventRepository(db=db)

    def create_ping_event(
        self,
        payload: PingIn,
        sticker_id: uuid.UUID,
        ip_hash: Optional[str],
        ua: Optional[str],
    ) -> PingEvent:
        return self.repo.create_ping_event(
            payload=payload, sticker_id=sticker_id, ip_hash=ip_hash, ua=ua
        )
