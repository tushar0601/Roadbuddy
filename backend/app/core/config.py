from __future__ import annotations

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):

    APP_NAME: str
    ENVIRONMENT: str
    DATABASE_URL: str
    SUPABASE_URL: str  
    SUPABASE_JWT_AUDIENCE: str = "authenticated"

    @property
    def SUPABASE_JWT_ISSUER(self) -> str:
        return f"{self.SUPABASE_URL.rstrip('/')}/auth/v1"

    @property
    def SUPABASE_JWKS_URL(self) -> str:
        return f"{self.SUPABASE_JWT_ISSUER}/.well-known/jwks.json"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
