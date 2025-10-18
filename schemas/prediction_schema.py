from pydantic import BaseModel, Field
from typing import List

'''
Creation of the base model for POST, GET, PUT and DELETE

'''

class StockHistory(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: float
    dividend_yield: float

class PredictionCreateBase(BaseModel):
    ticker: str
    history: List[StockHistory] = Field(..., description="Histórico de exatamente 5 dias")

class PredictionResponseBase(BaseModel):
    high: float
    low: float
