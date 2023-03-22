from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session
from ..schemas import User, ShowUser
from ..database import get_db
from ..crud import user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def user_create(request: User, db: Session = Depends(get_db)):
    return user.user_create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)