from fastapi import APIRouter

router = APIRouter(prefix='/rf')

@router.get('/prediction')
async def prediction():
    return {'test rf': 'test'}