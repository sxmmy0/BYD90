"""
AI Recommendation endpoints
"""
from fastapi import APIRouter

router = APIRouter()


# Recommendation endpoints will be implemented here
@router.get("/")
def get_recommendations():
    return {"message": "Recommendations endpoint - coming soon"}
