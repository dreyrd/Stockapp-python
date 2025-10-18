from api.v1.services.predicition_service_model import PredictionBaseModel

class RandomForestPrediction(PredictionBaseModel):
    def __init__(self):
        super().__init__('random_forest')
