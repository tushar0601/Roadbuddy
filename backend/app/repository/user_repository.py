from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.domain.user.model import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, user_email: EmailStr) -> User | None:
        return self.db.query(User).filter(User.email == user_email).first()
