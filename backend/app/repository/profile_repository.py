from __future__ import annotations

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.domain.profile.model import Profile


class ProfileRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_or_create_profile(
        self, supabase_user_id: str, email: str
    ) -> Optional[Profile]:
        email_val = email or ""
        stmt = (
            insert(Profile)
            .values(supabase_user_id=supabase_user_id, email=email_val)
            .on_conflict_do_update(
                index_elements=[Profile.supabase_user_id],
                set_={"email": email_val},
            )
            .returning(Profile)
        )
        result = self.db.execute(stmt).scalar_one()
        self.db.commit()
        return result
