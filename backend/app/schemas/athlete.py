"""
Athlete Pydantic schemas
"""
from pydantic import BaseModel

class Athlete(BaseModel):
    pass

class AthleteCreate(BaseModel):
    pass

class AthleteUpdate(BaseModel):
    pass

class AthleteProfile(BaseModel):
    pass

class AthleteStats(BaseModel):
    pass
