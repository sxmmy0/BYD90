"""
Athlete management endpoints
"""
from fastapi import APIRouter

router = APIRouter()


# Athlete endpoints will be implemented here
@router.get("/")
def get_athletes():
    return {"message": "Athletes endpoint - coming soon"}
