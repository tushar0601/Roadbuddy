from typing import Optional, List
from sqlalchemy.orm import Session
import uuid

from app.domain.ping_event.model import PingEvent, PingReason
from app.domain.ping_event.schema import PingIn


class PingEventRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_ping_event(
        self,
        payload: PingIn,
        sticker_id: uuid.UUID,
        ip_hash: Optional[str],
        ua: Optional[str],
    ) -> Optional[PingEvent]:

        pe = PingEvent(
            sticker_id=sticker_id,
            reason=payload.reason,
            note=payload.note,
            ip_hash=ip_hash if ip_hash else None,
            user_agent=(ua[:256] if ua else None),
        )

        self.db.add(pe)
        return pe
