"""
Authentication Pydantic schemas
"""
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Schema for JWT token response"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds until access token expires


class TokenData(BaseModel):
    """Schema for token data"""

    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None


class RefreshToken(BaseModel):
    """Schema for refresh token request"""

    refresh_token: str


class AccessToken(BaseModel):
    """Schema for access token response"""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class LoginResponse(BaseModel):
    """Schema for login response"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user: dict  # Will contain user information


class LogoutResponse(BaseModel):
    """Schema for logout response"""

    message: str = "Successfully logged out"


class TokenValidationResponse(BaseModel):
    """Schema for token validation response"""

    valid: bool
    user_id: Optional[int] = None
    expires_at: Optional[int] = None
