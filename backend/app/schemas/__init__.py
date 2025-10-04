"""
Pydantic schemas for API request/response models
"""
from .athlete import Athlete, AthleteCreate, AthleteProfile, AthleteStats, AthleteUpdate
from .auth import RefreshToken, Token, TokenData
from .coach import Coach, CoachCreate, CoachProfile, CoachSearch, CoachUpdate
from .community import (
    Comment,
    CommentCreate,
    Community,
    CommunityCreate,
    CommunityUpdate,
    Post,
    PostCreate,
    PostUpdate,
)
from .recommendation import (
    Recommendation,
    RecommendationCreate,
    RecommendationResponse,
    RecommendationUpdate,
)
from .user import (
    PasswordReset,
    PasswordResetConfirm,
    User,
    UserCreate,
    UserInDB,
    UserLogin,
    UserRegister,
    UserUpdate,
)

__all__ = [
    # User schemas
    "User",
    "UserCreate",
    "UserUpdate",
    "UserInDB",
    "UserLogin",
    "UserRegister",
    "PasswordReset",
    "PasswordResetConfirm",
    # Athlete schemas
    "Athlete",
    "AthleteCreate",
    "AthleteUpdate",
    "AthleteProfile",
    "AthleteStats",
    # Coach schemas
    "Coach",
    "CoachCreate",
    "CoachUpdate",
    "CoachProfile",
    "CoachSearch",
    # Auth schemas
    "Token",
    "TokenData",
    "RefreshToken",
    # Recommendation schemas
    "Recommendation",
    "RecommendationCreate",
    "RecommendationUpdate",
    "RecommendationResponse",
    # Community schemas
    "Community",
    "CommunityCreate",
    "CommunityUpdate",
    "Post",
    "PostCreate",
    "PostUpdate",
    "Comment",
    "CommentCreate",
]
