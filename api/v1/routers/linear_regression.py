from fastapi import APIRouter
from schemas.prediction_schema import PredictionCreateBase, PredictionResponseBase

router = APIRouter(prefix='/lr')

@router.post('/prediction', response_model=PredictionResponseBase)
async def linear_regression_prediction(prediction_post: PredictionCreateBase):
    
    prediction_result = PredictionResponseBase(
        high=prediction_post.high,
        low=prediction_post.low
    )
    return prediction_result