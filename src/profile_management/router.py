from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_profile_management():
    return {'message': 'profile_management router'}
