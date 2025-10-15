from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Stockapp-python')

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT, log_level='debug', reload=True)