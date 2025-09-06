"""
Coach model with specializations and athlete connections
"""
import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Boolean, Column, DateTime, Enum, ForeignKey, Integer, 
    JSON, String, Text, Float
)
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.athlete import Sport


class CoachLevel(str, enum.Enum):
    """Coach certification/experience level"""
    YOUTH = "youth"
    HIGH_SCHOOL = "high_school"
    COLLEGE = "college"
    PROFESSIONAL = "professional"
    RECREATIONAL = "recreational"


class CoachSpecialization(str, enum.Enum):
    """Coach specialization areas"""
    GENERAL_COACHING = "general_coaching"
    STRENGTH_CONDITIONING = "strength_conditioning"
    SKILLS_DEVELOPMENT = "skills_development"
    MENTAL_PERFORMANCE = "mental_performance"
    INJURY_PREVENTION = "injury_prevention"
    NUTRITION = "nutrition"
    RECOVERY = "recovery"
    YOUTH_DEVELOPMENT = "youth_development"


class Coach(Base):
    """
    Coach profile with specializations and athlete management
    """
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Professional Information
    license_number = Column(String(50), nullable=True)
    certifications = Column(JSON, nullable=True)  # List of coaching certifications
    specializations = Column(JSON, nullable=True)  # List of CoachSpecialization
    
    # Experience and Level
    coaching_level = Column(Enum(CoachLevel), nullable=False)
    years_coaching = Column(Integer, nullable=True)
    sports_coached = Column(JSON, nullable=True)  # List of Sport enums
    
    # Professional Details
    current_organization = Column(String(100), nullable=True)
    previous_organizations = Column(JSON, nullable=True)
    coaching_philosophy = Column(Text, nullable=True)
    
    # Contact and Availability
    hourly_rate = Column(Float, nullable=True)  # For paid coaching sessions
    availability = Column(JSON, nullable=True)  # Schedule availability
    time_zone = Column(String(50), nullable=True)
    
    # Performance and Ratings
    average_rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    success_stories = Column(JSON, nullable=True)
    
    # Settings and Preferences
    accepts_new_athletes = Column(Boolean, default=True)
    max_athletes = Column(Integer, nullable=True)
    preferred_athlete_level = Column(JSON, nullable=True)  # beginner, intermediate, etc.
    coaching_style = Column(JSON, nullable=True)  # tags describing coaching approach
    
    # Business Information (for professional coaches)
    business_name = Column(String(100), nullable=True)
    business_address = Column(Text, nullable=True)
    tax_id = Column(String(50), nullable=True)
    payment_methods = Column(JSON, nullable=True)
    
    # Verification Status
    is_verified = Column(Boolean, default=False)
    verification_documents = Column(JSON, nullable=True)
    background_check_status = Column(String(20), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="coach_profile")
    athlete_connections = relationship("CoachAthleteConnection", back_populates="coach")
    
    @property
    def current_athlete_count(self) -> int:
        """Get current number of connected athletes"""
        return len([conn for conn in self.athlete_connections if conn.is_active])
    
    @property
    def can_accept_athletes(self) -> bool:
        """Check if coach can accept new athletes"""
        if not self.accepts_new_athletes:
            return False
        if self.max_athletes and self.current_athlete_count >= self.max_athletes:
            return False
        return True

    def __repr__(self) -> str:
        return f"<Coach(id={self.id}, level='{self.coaching_level}', verified={self.is_verified})>"


class CoachAthleteConnection(Base):
    """
    Many-to-many relationship between coaches and athletes
    """
    __tablename__ = "coach_athlete_connections"

    id = Column(Integer, primary_key=True, index=True)
    coach_id = Column(Integer, ForeignKey("coaches.id"), nullable=False)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    
    # Connection Status
    is_active = Column(Boolean, default=True)
    connection_type = Column(String(20), default="coaching")  # coaching, mentoring, consulting
    
    # Connection Details
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    goals = Column(JSON, nullable=True)  # Shared goals for this coaching relationship
    
    # Payment and Billing (if applicable)
    is_paid_coaching = Column(Boolean, default=False)
    rate_per_session = Column(Float, nullable=True)
    sessions_completed = Column(Integer, default=0)
    
    # Performance Tracking
    progress_notes = Column(JSON, nullable=True)
    milestones = Column(JSON, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    coach = relationship("Coach", back_populates="athlete_connections")
    athlete = relationship("Athlete", back_populates="coach_connections")

    def __repr__(self) -> str:
        return f"<CoachAthleteConnection(coach_id={self.coach_id}, athlete_id={self.athlete_id}, active={self.is_active})>"
