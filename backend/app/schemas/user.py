"""
User Pydantic schemas for API request/response models
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator

from app.models.user import UserType


class UserBase(BaseModel):
    """Base user schema with common fields"""
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    user_type: UserType
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v
    
    @validator('username')
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if len(v) > 50:
            raise ValueError('Username must be less than 50 characters')
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('Username can only contain letters, numbers, hyphens, and underscores')
        return v


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    password: Optional[str] = None
    
    @validator('password')
    def validate_password(cls, v):
        if v is None:
            return v
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class User(UserBase):
    """Schema for user response"""
    id: int
    is_active: bool
    is_verified: bool
    is_premium: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    email_verified_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserInDB(User):
    """Schema for user in database (includes sensitive data)"""
    hashed_password: str
    verification_token: Optional[str] = None
    password_reset_token: Optional[str] = None
    password_reset_expires: Optional[datetime] = None


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    """Schema for user registration"""
    email: EmailStr
    username: str
    password: str
    confirm_password: str
    first_name: str
    last_name: str
    user_type: UserType
    phone_number: Optional[str] = None
    terms_accepted: bool = True
    
    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v
    
    @validator('terms_accepted')
    def terms_must_be_accepted(cls, v):
        if not v:
            raise ValueError('Terms and conditions must be accepted')
        return v


class PasswordReset(BaseModel):
    """Schema for password reset request"""
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    """Schema for password reset confirmation"""
    token: str
    new_password: str
    confirm_password: str
    
    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('Passwords do not match')
        return v


class EmailVerification(BaseModel):
    """Schema for email verification"""
    token: str


class UserProfile(BaseModel):
    """Schema for public user profile"""
    id: int
    username: str
    first_name: str
    last_name: str
    user_type: UserType
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserSearch(BaseModel):
    """Schema for user search results"""
    id: int
    username: str
    full_name: str
    user_type: UserType
    profile_picture: Optional[str] = None
    is_verified: bool
    
    class Config:
        from_attributes = True
