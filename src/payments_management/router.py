from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_payments_management():
    return {'message': 'payments_management router'}
