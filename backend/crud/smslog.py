from sqlalchemy.orm import Session
from .. import models
from ..schemas import SendSMS
from fastapi import HTTPException, status
from ..local_functions import send_sms_to_many

def sendsms(request: SendSMS, db: Session):
    print(f"SMS category with the name {request.text} is not found")
    receiver = db.query(models.Receiver).filter(models.Receiver.sms_category == request.sms_category).first()
    if not receiver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"SMS category with the name {request.sms_category} is not found")
    
    try:
        send_sms_to_many(src=request.source_addr, dest_list=receiver.number_list, message=request.text)
    except Exception as e: print(e)


    new_smslog = models.SMSlog(receiver_id=receiver.id, user_id=1, text=request.text, source_addr=request.source_addr)
    db.add(new_smslog)
    db.commit()
    db.refresh(new_smslog)
    return new_smslog



def get_smslog(db: Session):
    smslogs = db.query(models.SMSlog).all()
    return smslogs