import uuid
from sqlalchemy.orm import Session
from pydantic import EmailStr

from app.repository.user_repository import UserRepository
from app.domain.user.model import User
from app.domain.auth.schema import SignUpIn


class UserService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db=db)

    def get_by_email(self, user_email: EmailStr) -> User | None:
        return self.repo.get_by_email(user_email=user_email)
