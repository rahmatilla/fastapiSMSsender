from fastapi import Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..schemas import SMSReceivers
from ..database import get_db
from ..oauth2 import get_current_user
from ..crud import smsreceivers

router = APIRouter(
    prefix='/smsreceiver',
    tags=['smsreceiver']
)

@router.post('/', status_code=status.HTTP_201_CREATED) 
async def create(request: SMSReceivers, db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    #print(current_user)
    return smsreceivers.create(request, db)

@router.get('/')
async def get_all(db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smsreceivers.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_one(id: int, db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smsreceivers.get_one(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smsreceivers.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: SMSReceivers, db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smsreceivers.update(id, request, db)



