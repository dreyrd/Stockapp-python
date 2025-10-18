from api.v1.services.predicition_service_model import PredictionBaseModel

class LinearRegressionPrediction(PredictionBaseModel):
    def __init__(self):
        super().__init__('linear_model_lags_less_features.pkl')
