"""
AI Recommendation model for personalized athlete suggestions
"""
import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Boolean, Column, DateTime, Enum, Float, ForeignKey, 
    Integer, JSON, String, Text
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class RecommendationType(str, enum.Enum):
    """Types of recommendations the AI can provide"""
    FITNESS = "fitness"
    SKILL_DEVELOPMENT = "skill_development" 
    RECOVERY = "recovery"
    NUTRITION = "nutrition"
    MENTAL_PERFORMANCE = "mental_performance"
    INJURY_PREVENTION = "injury_prevention"
    EQUIPMENT = "equipment"
    TRAINING_SCHEDULE = "training_schedule"
    GOAL_SETTING = "goal_setting"


class RecommendationPriority(str, enum.Enum):
    """Priority levels for recommendations"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class RecommendationStatus(str, enum.Enum):
    """Status of recommendation implementation"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    DISMISSED = "dismissed"
    EXPIRED = "expired"


class Recommendation(Base):
    """
    AI-powered recommendations for athletes based on their profile and goals
    """
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    
    # Recommendation Details
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    recommendation_type = Column(Enum(RecommendationType), nullable=False)
    priority = Column(Enum(RecommendationPriority), default=RecommendationPriority.MEDIUM)
    
    # AI Generation Details
    ai_model_version = Column(String(50), nullable=True)  # Track which AI model generated this
    confidence_score = Column(Float, nullable=True)  # AI confidence in recommendation (0.0-1.0)
    reasoning = Column(Text, nullable=True)  # AI's reasoning for this recommendation
    
    # Structured Data
    action_items = Column(JSON, nullable=True)  # Specific steps to follow
    resources = Column(JSON, nullable=True)     # Links, videos, articles
    metrics_to_track = Column(JSON, nullable=True)  # What to measure for progress
    
    # Personalization Factors
    based_on_factors = Column(JSON, nullable=True)  # What athlete data influenced this
    sport_specific = Column(Boolean, default=True)
    position_specific = Column(Boolean, default=True)
    
    # Implementation Details
    estimated_duration = Column(Integer, nullable=True)  # in days
    difficulty_level = Column(String(20), nullable=True)  # easy, medium, hard
    required_equipment = Column(JSON, nullable=True)
    
    # Status and Tracking
    status = Column(Enum(RecommendationStatus), default=RecommendationStatus.PENDING)
    implementation_notes = Column(Text, nullable=True)
    athlete_feedback = Column(JSON, nullable=True)  # Rating, comments from athlete
    
    # Effectiveness Tracking
    effectiveness_rating = Column(Float, nullable=True)  # Athlete's rating (1-5)
    measurable_improvement = Column(JSON, nullable=True)  # Quantifiable improvements
    
    # Scheduling
    scheduled_for = Column(DateTime, nullable=True)  # When to start
    expires_at = Column(DateTime, nullable=True)    # When recommendation becomes outdated
    completed_at = Column(DateTime, nullable=True)
    
    # Visibility and Sharing
    is_visible_to_coach = Column(Boolean, default=True)
    coach_comments = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    athlete = relationship("Athlete", back_populates="recommendations")

    @property
    def is_expired(self) -> bool:
        """Check if recommendation has expired"""
        if self.expires_at:
            return datetime.utcnow() > self.expires_at
        return False

    @property
    def days_since_created(self) -> int:
        """Calculate days since recommendation was created"""
        return (datetime.utcnow() - self.created_at).days

    def __repr__(self) -> str:
        return f"<Recommendation(id={self.id}, type='{self.recommendation_type}', priority='{self.priority}')>"


class RecommendationFeedback(Base):
    """
    Detailed feedback on recommendations for AI model improvement
    """
    __tablename__ = "recommendation_feedback"

    id = Column(Integer, primary_key=True, index=True)
    recommendation_id = Column(Integer, ForeignKey("recommendations.id"), nullable=False)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    
    # Feedback Details
    rating = Column(Integer, nullable=False)  # 1-5 star rating
    usefulness = Column(Integer, nullable=True)  # 1-5 how useful was it
    accuracy = Column(Integer, nullable=True)   # 1-5 how accurate was it
    clarity = Column(Integer, nullable=True)    # 1-5 how clear was it
    
    # Text Feedback
    comments = Column(Text, nullable=True)
    what_worked = Column(Text, nullable=True)
    what_didnt_work = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)
    
    # Implementation Results
    implemented = Column(Boolean, default=False)
    implementation_difficulty = Column(Integer, nullable=True)  # 1-5
    results_achieved = Column(JSON, nullable=True)
    time_to_see_results = Column(Integer, nullable=True)  # in days
    
    # Context
    feedback_context = Column(JSON, nullable=True)  # Additional context data
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<RecommendationFeedback(recommendation_id={self.recommendation_id}, rating={self.rating})>"
