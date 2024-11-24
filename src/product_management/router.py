from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_product_management():
    return {'message': 'product_management router'}
