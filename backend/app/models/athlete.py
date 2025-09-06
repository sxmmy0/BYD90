"""
Athlete model with sports, positions, and performance data
"""
import enum
from datetime import datetime, date
from typing import Optional

from sqlalchemy import (
    Boolean, Column, Date, DateTime, Enum, Float, ForeignKey, 
    Integer, JSON, String, Text
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Sport(str, enum.Enum):
    """Sports enumeration"""
    FOOTBALL = "football"
    BASKETBALL = "basketball"
    SOCCER = "soccer"
    TENNIS = "tennis"
    VOLLEYBALL = "volleyball"
    BASEBALL = "baseball"
    HOCKEY = "hockey"
    SWIMMING = "swimming"
    TRACK_FIELD = "track_field"
    GOLF = "golf"


class AthletePosition(str, enum.Enum):
    """Position enumeration for different sports"""
    # Football
    QUARTERBACK = "quarterback"
    RUNNING_BACK = "running_back"
    WIDE_RECEIVER = "wide_receiver"
    TIGHT_END = "tight_end"
    OFFENSIVE_LINE = "offensive_line"
    DEFENSIVE_LINE = "defensive_line"
    LINEBACKER = "linebacker"
    CORNERBACK = "cornerback"
    SAFETY = "safety"
    KICKER = "kicker"
    PUNTER = "punter"
    
    # Basketball
    POINT_GUARD = "point_guard"
    SHOOTING_GUARD = "shooting_guard"
    SMALL_FORWARD = "small_forward"
    POWER_FORWARD = "power_forward"
    CENTER = "center"
    
    # Soccer
    GOALKEEPER = "goalkeeper"
    DEFENDER = "defender"
    MIDFIELDER = "midfielder"
    FORWARD = "forward"
    
    # Tennis
    SINGLES = "singles"
    DOUBLES = "doubles"
    
    # General/Other
    GENERAL = "general"


class Athlete(Base):
    """
    Athlete profile with sports-specific information and performance metrics
    """
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Basic Athletic Information
    primary_sport = Column(Enum(Sport), nullable=False)
    secondary_sports = Column(JSON, nullable=True)  # List of additional sports
    primary_position = Column(Enum(AthletePosition), nullable=False)
    secondary_positions = Column(JSON, nullable=True)  # List of additional positions
    
    # Physical Attributes
    height = Column(Float, nullable=True)  # in cm
    weight = Column(Float, nullable=True)  # in kg
    date_of_birth = Column(Date, nullable=True)
    dominant_hand = Column(String(10), nullable=True)  # left, right, ambidextrous
    
    # Experience and Level
    experience_level = Column(String(20), nullable=True)  # beginner, intermediate, advanced, professional
    years_playing = Column(Integer, nullable=True)
    current_team = Column(String(100), nullable=True)
    jersey_number = Column(String(10), nullable=True)
    
    # Performance Metrics (JSON for flexibility)
    fitness_metrics = Column(JSON, nullable=True)  # speed, strength, endurance, etc.
    skill_metrics = Column(JSON, nullable=True)    # sport-specific skills
    game_stats = Column(JSON, nullable=True)       # recent game statistics
    
    # Goals and Preferences
    training_goals = Column(JSON, nullable=True)   # List of training objectives
    training_frequency = Column(Integer, nullable=True)  # sessions per week
    preferred_training_time = Column(String(20), nullable=True)  # morning, afternoon, evening
    
    # Injury and Recovery
    injury_history = Column(JSON, nullable=True)   # Past injuries
    current_injuries = Column(JSON, nullable=True) # Current limitations
    recovery_status = Column(String(20), nullable=True)  # active, recovering, injured
    
    # Settings and Preferences
    privacy_settings = Column(JSON, nullable=True)
    notification_preferences = Column(JSON, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="athlete_profile")
    recommendations = relationship("Recommendation", back_populates="athlete")
    coach_connections = relationship("CoachAthleteConnection", back_populates="athlete")

    @property
    def age(self) -> Optional[int]:
        """Calculate age from date of birth"""
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

    @property
    def bmi(self) -> Optional[float]:
        """Calculate BMI if height and weight are available"""
        if self.height and self.weight:
            height_m = self.height / 100  # convert cm to meters
            return round(self.weight / (height_m ** 2), 2)
        return None

    def __repr__(self) -> str:
        return f"<Athlete(id={self.id}, sport='{self.primary_sport}', position='{self.primary_position}')>"
