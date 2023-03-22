from fastapi import Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..schemas import Receiver, ShowReceiver, User
from ..database import get_db
from ..oauth2 import get_current_user
from ..crud import receiver

router = APIRouter(
    prefix='/receiver',
    tags=['receiver']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: Receiver, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return receiver.create(request, db)

@router.get('/')
async def get_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return receiver.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowReceiver)
async def get_one(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return receiver.get_one(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return receiver.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: Receiver, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return receiver.update(id, request, db)



