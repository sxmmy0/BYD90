"""
Avatar and customization models for user personalization
"""
import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class AvatarStyle(str, enum.Enum):
    """Available avatar styles"""

    REALISTIC = "realistic"
    CARTOON = "cartoon"
    PIXEL_ART = "pixel_art"
    MINIMALIST = "minimalist"
    SPORTS_THEMED = "sports_themed"


class AvatarGender(str, enum.Enum):
    """Avatar gender options"""

    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    CUSTOM = "custom"


class Avatar(Base):
    """
    User avatar with customizable features
    """

    __tablename__ = "avatars"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), unique=True, nullable=False
    )

    # Basic Avatar Properties
    name = Column(String(100), nullable=True)  # Custom name for avatar
    style = Column(Enum(AvatarStyle), default=AvatarStyle.REALISTIC)
    gender = Column(Enum(AvatarGender), default=AvatarGender.MALE)

    # Physical Appearance (JSON for flexibility)
    physical_features = Column(
        JSON, nullable=True
    )  # skin tone, body type, etc.
    facial_features = Column(JSON, nullable=True)  # eyes, nose, mouth, etc.
    hair = Column(JSON, nullable=True)  # style, color, length

    # Clothing and Accessories
    outfit = Column(JSON, nullable=True)  # current outfit configuration
    accessories = Column(JSON, nullable=True)  # jewelry, glasses, etc.
    sports_gear = Column(
        JSON, nullable=True
    )  # sport-specific equipment/clothing

    # Unlocked Content
    unlocked_items = Column(JSON, nullable=True)  # Items available to user
    purchased_items = Column(JSON, nullable=True)  # Premium items bought
    earned_items = Column(
        JSON, nullable=True
    )  # Items earned through achievements

    # Avatar Status and Progression
    level = Column(Integer, default=1)
    experience_points = Column(Integer, default=0)
    achievements = Column(JSON, nullable=True)  # Avatar-related achievements

    # Preferences
    is_public = Column(Boolean, default=True)  # Show avatar to other users
    allow_customization_suggestions = Column(Boolean, default=True)

    # Generated Assets
    avatar_image_url = Column(
        String(500), nullable=True
    )  # Generated avatar image
    thumbnail_url = Column(String(500), nullable=True)  # Small version
    last_generated = Column(
        DateTime, nullable=True
    )  # When image was last generated

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    user = relationship("User", back_populates="avatar")
    customizations = relationship(
        "AvatarCustomization", back_populates="avatar"
    )

    def __repr__(self) -> str:
        return f"<Avatar(id={self.id}, user_id={self.user_id}, style='{self.style}')>"


class AvatarCustomization(Base):
    """
    Track avatar customization history and variations
    """

    __tablename__ = "avatar_customizations"

    id = Column(Integer, primary_key=True, index=True)
    avatar_id = Column(Integer, ForeignKey("avatars.id"), nullable=False)

    # Customization Details
    customization_name = Column(String(100), nullable=True)  # User-given name
    description = Column(String(500), nullable=True)

    # Complete Avatar Configuration
    full_configuration = Column(JSON, nullable=False)  # Complete avatar setup

    # Metadata
    is_favorite = Column(Boolean, default=False)
    is_current = Column(Boolean, default=False)
    usage_count = Column(
        Integer, default=0
    )  # How many times this config was used

    # Sharing and Social
    is_shareable = Column(Boolean, default=False)
    shared_publicly = Column(Boolean, default=False)
    likes_count = Column(Integer, default=0)

    # Generated Assets for this Configuration
    preview_image_url = Column(String(500), nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    last_used = Column(DateTime, nullable=True)

    # Relationships
    avatar = relationship("Avatar", back_populates="customizations")

    def __repr__(self) -> str:
        return f"<AvatarCustomization(id={self.id}, avatar_id={self.avatar_id}, current={self.is_current})>"


class AvatarItem(Base):
    """
    Available avatar items (clothing, accessories, etc.)
    """

    __tablename__ = "avatar_items"

    id = Column(Integer, primary_key=True, index=True)

    # Item Details
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    category = Column(
        String(50), nullable=False
    )  # clothing, accessory, hair, etc.
    subcategory = Column(String(50), nullable=True)  # shirt, pants, hat, etc.

    # Item Properties
    rarity = Column(
        String(20), default="common"
    )  # common, rare, epic, legendary
    sport_specific = Column(
        String(50), nullable=True
    )  # If item is sport-specific
    gender_restriction = Column(Enum(AvatarGender), nullable=True)

    # Availability and Pricing
    is_free = Column(Boolean, default=True)
    cost_in_coins = Column(Integer, nullable=True)  # In-app currency
    cost_in_real_money = Column(Integer, nullable=True)  # In cents
    requires_achievement = Column(
        String(100), nullable=True
    )  # Achievement needed to unlock

    # Item Data
    asset_data = Column(JSON, nullable=False)  # Visual/3D model data
    compatibility = Column(
        JSON, nullable=True
    )  # What styles/other items it works with

    # Metadata
    is_active = Column(Boolean, default=True)
    popularity_score = Column(Integer, default=0)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self) -> str:
        return f"<AvatarItem(id={self.id}, name='{self.name}', category='{self.category}')>"
