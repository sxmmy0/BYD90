"""
Community Pydantic schemas
"""
from pydantic import BaseModel


class Community(BaseModel):
    pass


class CommunityCreate(BaseModel):
    pass


class CommunityUpdate(BaseModel):
    pass


class Post(BaseModel):
    pass


class PostCreate(BaseModel):
    pass


class PostUpdate(BaseModel):
    pass


class Comment(BaseModel):
    pass


class CommentCreate(BaseModel):
    pass
