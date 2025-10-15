from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from core.configs import settings


app = FastAPI(title='Stockapp-python')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/teste')
async def teste():
    return {'Olaa': 'testee'}

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT, log_level='debug', reload=True)