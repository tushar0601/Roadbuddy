import uuid
from typing import Optional, List
from sqlalchemy.orm import Session
from app.repository.notification_repository import NotificationRepository
from app.domain.notification.model import Notification


class NotificationService:

    def __init__(self, db: Session):
        self.repo = NotificationRepository(db=db)

    def create_notification(self, data: Notification) -> Optional[Notification]:
        return self.repo.create_notification(data=data)

    def get_notifications(self, user_id: uuid.UUID) -> List[Notification]:
        return self.repo.get_notifications(user_id=user_id)
