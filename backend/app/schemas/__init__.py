"""
Pydantic schemas for API request/response models
"""
from .user import (
    User, UserCreate, UserUpdate, UserInDB, 
    UserLogin, UserRegister, PasswordReset, PasswordResetConfirm
)
from .athlete import (
    Athlete, AthleteCreate, AthleteUpdate,
    AthleteProfile, AthleteStats
)
from .coach import (
    Coach, CoachCreate, CoachUpdate,
    CoachProfile, CoachSearch
)
from .auth import Token, TokenData, RefreshToken
from .recommendation import (
    Recommendation, RecommendationCreate, RecommendationUpdate,
    RecommendationResponse
)
from .community import (
    Community, CommunityCreate, CommunityUpdate,
    Post, PostCreate, PostUpdate,
    Comment, CommentCreate
)

__all__ = [
    # User schemas
    "User", "UserCreate", "UserUpdate", "UserInDB",
    "UserLogin", "UserRegister", "PasswordReset", "PasswordResetConfirm",
    
    # Athlete schemas
    "Athlete", "AthleteCreate", "AthleteUpdate",
    "AthleteProfile", "AthleteStats",
    
    # Coach schemas  
    "Coach", "CoachCreate", "CoachUpdate",
    "CoachProfile", "CoachSearch",
    
    # Auth schemas
    "Token", "TokenData", "RefreshToken",
    
    # Recommendation schemas
    "Recommendation", "RecommendationCreate", "RecommendationUpdate",
    "RecommendationResponse",
    
    # Community schemas
    "Community", "CommunityCreate", "CommunityUpdate",
    "Post", "PostCreate", "PostUpdate",
    "Comment", "CommentCreate",
]
