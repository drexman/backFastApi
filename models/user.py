from datetime import datetime
from pydantic import BaseModel, Field

class User(BaseModel):
    _id: str
    name: str = Field(max_length=255, null=False)
    email: str = Field(max_length=255, null=False, unique=True)
    password: str = Field(default=None, null=False)
    is_admin: bool = Field(default=False)
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    refresh_token: str = Field(null=True)

class UserLoginSchema(BaseModel):
    email: str
    password: str