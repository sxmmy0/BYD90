"""
Coach management endpoints
"""
from fastapi import APIRouter

router = APIRouter()


# Coach endpoints will be implemented here
@router.get("/")
def get_coaches():
    return {"message": "Coaches endpoint - coming soon"}
