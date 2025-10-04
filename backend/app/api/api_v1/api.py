"""
Main API router that includes all endpoint routers
"""
from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    athletes,
    auth,
    coaches,
    communities,
    recommendations,
    users,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    athletes.router, prefix="/athletes", tags=["athletes"]
)
api_router.include_router(coaches.router, prefix="/coaches", tags=["coaches"])
api_router.include_router(
    recommendations.router, prefix="/recommendations", tags=["recommendations"]
)
api_router.include_router(
    communities.router, prefix="/communities", tags=["communities"]
)
