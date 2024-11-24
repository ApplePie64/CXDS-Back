from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_order_management():
    return {'message': 'order_management router'}
