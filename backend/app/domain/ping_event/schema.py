from pydantic import BaseModel, Field
from typing import Literal

PingReason = Literal["BLOCKED", "WRONG_PARKING", "EMERGENCY"]

class PingIn(BaseModel):
    reason: PingReason
    note: str | None = Field(default=None, max_length=300)
