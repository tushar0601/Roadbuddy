from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import jwt
from jwt import PyJWKClient
from jwt.exceptions import InvalidTokenError
from app.core.config import settings


@dataclass(frozen=True)
class SupabaseClaims:
    sub: str
    email: Optional[str]
    role: Optional[str]
    raw: Dict[str, Any]


_jwk_client: Optional[PyJWKClient] = None


def _get_jwk_client() -> PyJWKClient:
    global _jwk_client
    if _jwk_client is None:
        # PyJWKClient internally caches fetched JWKS
        _jwk_client = PyJWKClient(settings.SUPABASE_JWKS_URL)
    return _jwk_client


def verify_supabase_jwt(token: str) -> SupabaseClaims:
    """
    Verify Supabase access token (JWT) using project's JWKS.
    Validates signature + exp + iss + aud.
    """
    jwk_client = _get_jwk_client()
    signing_key = jwk_client.get_signing_key_from_jwt(token).key

    try:
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256", "ES256"],  
            audience=settings.SUPABASE_JWT_AUDIENCE,
            issuer=settings.SUPABASE_JWT_ISSUER,
            options={
                "require": ["exp", "sub", "iss", "aud"],
            },
        )
    except InvalidTokenError as e:
        raise ValueError(f"Invalid Supabase token: {str(e)}") from e

    return SupabaseClaims(
        sub=str(payload.get("sub")),
        email=payload.get("email"),
        role=payload.get("role"),
        raw=payload,
    )
