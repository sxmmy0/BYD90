"""
User model for authentication and base user information
"""
import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserType(str, enum.Enum):
    """User type enumeration"""
    ATHLETE = "athlete"
    COACH = "coach"
    ADMIN = "admin"


class User(Base):
    """
    Base user model for authentication and common user data
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    # Profile Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    profile_picture = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    phone_number = Column(String(20), nullable=True)
    
    # User Type and Status
    user_type = Column(Enum(UserType), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Verification
    email_verified_at = Column(DateTime, nullable=True)
    verification_token = Column(String(255), nullable=True)
    password_reset_token = Column(String(255), nullable=True)
    password_reset_expires = Column(DateTime, nullable=True)
    
    # Relationships
    athlete_profile = relationship("Athlete", back_populates="user", uselist=False)
    coach_profile = relationship("Coach", back_populates="user", uselist=False)
    avatar = relationship("Avatar", back_populates="user", uselist=False)
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    community_memberships = relationship("CommunityMember", back_populates="user")

    @property
    def full_name(self) -> str:
        """Get user's full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def display_name(self) -> str:
        """Get user's display name (full name or username)"""
        if self.first_name and self.last_name:
            return self.full_name
        return self.username

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', type='{self.user_type}')>"
