from pydantic.v1 import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = 'api/v1'
    PORT: int = int(os.getenv('PORT'))
    HOST: str = os.getenv('HOST')
    
    class Config:
        case_sensitive = False
        venv_file = 'venv'
        
settings = Settings()