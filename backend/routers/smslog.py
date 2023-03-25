from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session
from ..schemas import SendSMS
from ..database import get_db
from ..oauth2 import get_current_user
from ..crud import smslog

router = APIRouter(
    prefix='/sendsms',
    tags=['sendsms']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def sendsms(request: SendSMS, db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smslog.sendsms(request, db)

@router.get('/')
async def get_smslog(db: Session = Depends(get_db)): #, current_user: User = Depends(get_current_user)
    return smslog.get_smslog(db)