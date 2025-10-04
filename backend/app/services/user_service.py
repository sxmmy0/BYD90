"""
User service for database operations
"""
from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User, UserType
from app.schemas.user import UserCreate, UserUpdate


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Get user by username"""
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user_create: UserCreate) -> User:
    """Create a new user"""
    hashed_password = get_password_hash(user_create.password)

    db_user = User(
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed_password,
        first_name=user_create.first_name,
        last_name=user_create.last_name,
        user_type=user_create.user_type,
        phone_number=user_create.phone_number,
        bio=user_create.bio,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(
    db: Session, user_id: int, user_update: UserUpdate
) -> Optional[User]:
    """Update user information"""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    update_data = user_update.dict(exclude_unset=True)

    # Hash password if provided
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(
            update_data.pop("password")
        )

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(
    db: Session, email: str, password: str
) -> Optional[User]:
    """Authenticate user with email and password"""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, str(user.hashed_password)):
        return None
    return user


def verify_user_email(db: Session, user_id: int) -> Optional[User]:
    """Mark user email as verified"""
    from datetime import datetime

    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    setattr(db_user, "is_verified", True)
    setattr(db_user, "email_verified_at", datetime.utcnow())
    setattr(db_user, "verification_token", None)

    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_password(
    db: Session, user_id: int, new_password: str
) -> Optional[User]:
    """Update user password"""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    setattr(db_user, "hashed_password", get_password_hash(new_password))
    setattr(db_user, "password_reset_token", None)
    setattr(db_user, "password_reset_expires", None)

    db.commit()
    db.refresh(db_user)
    return db_user


def deactivate_user(db: Session, user_id: int) -> Optional[User]:
    """Deactivate user account"""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    setattr(db_user, "is_active", False)
    db.commit()
    db.refresh(db_user)
    return db_user


def activate_user(db: Session, user_id: int) -> Optional[User]:
    """Activate user account"""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    setattr(db_user, "is_active", True)
    db.commit()
    db.refresh(db_user)
    return db_user
