"""
Recommendation Pydantic schemas
"""
from pydantic import BaseModel

class Recommendation(BaseModel):
    pass

class RecommendationCreate(BaseModel):
    pass

class RecommendationUpdate(BaseModel):
    pass

class RecommendationResponse(BaseModel):
    pass
