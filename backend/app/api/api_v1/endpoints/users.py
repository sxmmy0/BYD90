"""
User management endpoints
"""
from fastapi import APIRouter

router = APIRouter()

# User endpoints will be implemented here
@router.get("/")
def get_users():
    return {"message": "Users endpoint - coming soon"}
