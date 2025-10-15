from pydantic import BaseModel

class PredictionCreateBase(BaseModel):
    high: float
    low: float

class PredictionResponseBase(BaseModel):
    high: float
    low: float
