"""
FastAPI dependencies for authentication and database access
"""
from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.security import verify_token
from app.models.user import User
from app.services.user_service import get_user_by_id

# Security scheme
security = HTTPBearer()


def get_db() -> Generator:
    """
    Database dependency
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_current_user(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    """
    Get the current authenticated user from JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Extract token from credentials
        token = credentials.credentials

        # Verify token and get user ID
        user_id = verify_token(token)
        if user_id is None:
            raise credentials_exception

        # Get user from database
        user = get_user_by_id(db, user_id=int(user_id))
        if user is None:
            raise credentials_exception

        return user

    except Exception:
        raise credentials_exception


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Get the current active user (must be active and verified)
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    return current_user


def get_current_athlete(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Get the current user if they are an athlete
    """
    if current_user.user_type != "athlete":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access restricted to athletes only",
        )
    return current_user


def get_current_coach(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Get the current user if they are a coach
    """
    if current_user.user_type != "coach":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access restricted to coaches only",
        )
    return current_user


def get_current_admin(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Get the current user if they are an admin
    """
    if current_user.user_type != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access restricted to administrators only",
        )
    return current_user


def get_current_verified_user(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Get the current user if they are verified
    """
    if not current_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email verification required",
        )
    return current_user


def get_optional_current_user(
    db: Session = Depends(get_db),
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Optional[User]:
    """
    Get the current user if authenticated, otherwise return None
    Useful for endpoints that work for both authenticated and anonymous users
    """
    if not credentials:
        return None

    try:
        token = credentials.credentials
        user_id = verify_token(token)
        if user_id is None:
            return None

        user = get_user_by_id(db, user_id=int(user_id))
        return user

    except Exception:
        return None
