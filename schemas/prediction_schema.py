from pydantic import BaseModel

'''
Creation of the base model for POST, GET, PUT and DELETE

'''

class PredictionCreateBase(BaseModel):
    high: float
    low: float

class PredictionResponseBase(BaseModel):
    high: float
    low: float
