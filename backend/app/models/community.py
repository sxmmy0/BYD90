"""
Community, posts, and social interaction models
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
    Text,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class CommunityType(str, enum.Enum):
    """Types of communities"""

    SPORT_SPECIFIC = "sport_specific"
    POSITION_SPECIFIC = "position_specific"
    SKILL_LEVEL = "skill_level"
    GEOGRAPHIC = "geographic"
    TEAM_BASED = "team_based"
    GENERAL = "general"
    TRAINING_GROUP = "training_group"


class CommunityPrivacy(str, enum.Enum):
    """Community privacy levels"""

    PUBLIC = "public"
    PRIVATE = "private"
    INVITE_ONLY = "invite_only"


class PostType(str, enum.Enum):
    """Types of posts"""

    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    ACHIEVEMENT = "achievement"
    WORKOUT = "workout"
    PROGRESS = "progress"
    QUESTION = "question"
    TIP = "tip"
    POLL = "poll"


class Community(Base):
    """
    Communities for athletes and coaches to connect and share
    """

    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Information
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    community_type = Column(Enum(CommunityType), nullable=False)
    privacy = Column(Enum(CommunityPrivacy), default=CommunityPrivacy.PUBLIC)

    # Community Settings
    tags = Column(JSON, nullable=True)  # Sport, skill level, location tags
    rules = Column(JSON, nullable=True)  # Community guidelines
    welcome_message = Column(Text, nullable=True)

    # Media
    cover_image_url = Column(String(500), nullable=True)
    icon_url = Column(String(500), nullable=True)

    # Moderation
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    moderator_ids = Column(
        JSON, nullable=True
    )  # List of user IDs who can moderate
    is_moderated = Column(Boolean, default=True)
    auto_approve_posts = Column(Boolean, default=True)

    # Statistics
    member_count = Column(Integer, default=0)
    post_count = Column(Integer, default=0)
    active_members_30d = Column(Integer, default=0)

    # Status
    is_active = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    last_activity = Column(DateTime, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[creator_id])
    members = relationship("CommunityMember", back_populates="community")
    posts = relationship("Post", back_populates="community")

    def __repr__(self) -> str:
        return f"<Community(id={self.id}, name='{self.name}', type='{self.community_type}')>"


class CommunityMember(Base):
    """
    Membership relationship between users and communities
    """

    __tablename__ = "community_members"

    id = Column(Integer, primary_key=True, index=True)
    community_id = Column(
        Integer, ForeignKey("communities.id"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Membership Details
    role = Column(String(20), default="member")  # member, moderator, admin
    joined_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Engagement
    post_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    last_active = Column(DateTime, default=datetime.utcnow)

    # Settings
    notification_preferences = Column(JSON, nullable=True)
    is_muted = Column(Boolean, default=False)

    # Relationships
    community = relationship("Community", back_populates="members")
    user = relationship("User", back_populates="community_memberships")

    def __repr__(self) -> str:
        return f"<CommunityMember(community_id={self.community_id}, user_id={self.user_id}, role='{self.role}')>"


class Post(Base):
    """
    Posts within communities
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    community_id = Column(
        Integer, ForeignKey("communities.id"), nullable=False
    )
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Post Content
    title = Column(String(200), nullable=True)
    content = Column(Text, nullable=False)
    post_type = Column(Enum(PostType), default=PostType.TEXT)

    # Media and Attachments
    media_urls = Column(JSON, nullable=True)  # Images, videos, etc.
    attachments = Column(JSON, nullable=True)  # Files, workout data, etc.

    # Engagement
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
    view_count = Column(Integer, default=0)

    # Moderation
    is_approved = Column(Boolean, default=True)
    is_pinned = Column(Boolean, default=False)
    is_locked = Column(Boolean, default=False)  # No more comments
    moderation_notes = Column(Text, nullable=True)

    # Tags and Categories
    tags = Column(JSON, nullable=True)
    mentioned_users = Column(JSON, nullable=True)  # User IDs mentioned in post

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    community = relationship("Community", back_populates="posts")
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("PostLike", back_populates="post")

    def __repr__(self) -> str:
        return f"<Post(id={self.id}, type='{self.post_type}', author_id={self.author_id})>"


class Comment(Base):
    """
    Comments on posts
    """

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    parent_comment_id = Column(
        Integer, ForeignKey("comments.id"), nullable=True
    )  # For replies

    # Comment Content
    content = Column(Text, nullable=False)

    # Engagement
    like_count = Column(Integer, default=0)
    reply_count = Column(Integer, default=0)

    # Moderation
    is_approved = Column(Boolean, default=True)
    moderation_notes = Column(Text, nullable=True)

    # Mentions
    mentioned_users = Column(JSON, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")
    parent_comment = relationship("Comment", remote_side=[id])
    replies = relationship("Comment", remote_side=[parent_comment_id])
    likes = relationship("CommentLike", back_populates="comment")

    def __repr__(self) -> str:
        return f"<Comment(id={self.id}, post_id={self.post_id}, author_id={self.author_id})>"


class PostLike(Base):
    """
    Likes on posts
    """

    __tablename__ = "post_likes"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    post = relationship("Post", back_populates="likes")
    user = relationship("User")

    def __repr__(self) -> str:
        return f"<PostLike(post_id={self.post_id}, user_id={self.user_id})>"


class CommentLike(Base):
    """
    Likes on comments
    """

    __tablename__ = "comment_likes"

    id = Column(Integer, primary_key=True, index=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    comment = relationship("Comment", back_populates="likes")
    user = relationship("User")

    def __repr__(self) -> str:
        return f"<CommentLike(comment_id={self.comment_id}, user_id={self.user_id})>"
