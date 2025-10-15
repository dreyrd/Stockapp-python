from fastapi import APIRouter

router = APIRouter(prefix='/lr')

@router.get('/prediction')
async def prediction():
    return {'test lr': 'test'}