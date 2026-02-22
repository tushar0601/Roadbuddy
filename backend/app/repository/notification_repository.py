from typing import Optional, List
from sqlalchemy.orm import Session
import uuid
from app.domain.notification.model import Notification


class NotificationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_notification(self, data: Notification) -> Optional[Notification]:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def get_notifications(self, user_id: uuid.UUID) -> List[Notification]:
        return self.db.query(Notification).filter(Notification.user_id == user_id).all()
