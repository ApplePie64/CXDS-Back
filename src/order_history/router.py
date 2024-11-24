from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_order_history():
    return {'message': 'order_history router'}
