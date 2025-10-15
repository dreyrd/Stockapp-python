from fastapi import APIRouter
from schemas.prediction_schema import PredictionCreateBase, PredictionResponseBase

router = APIRouter(prefix='/rf')

# Endpoint to make a post for a prediction in the random forest model
@router.post('/prediction', response_model=PredictionResponseBase)
async def random_forest_prediction(prediction_post: PredictionCreateBase):
    
    prediction_result = PredictionResponseBase(
        high=prediction_post.high,
        low=prediction_post.low
    )
    return prediction_result