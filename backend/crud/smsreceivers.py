from sqlalchemy.orm import Session
from .. import models
from ..schemas import SMSReceivers
from fastapi import HTTPException, status


def create(request: SMSReceivers, db: Session):
    new_smsreceiver = models.SMSReceivers(network=request.network, criteria=request.criteria, notification=request.notification,
                                          tel_number=request.tel_number, name=request.name)
    db.add(new_smsreceiver)
    db.commit()
    db.refresh(new_smsreceiver)
    return new_smsreceiver


def get_all(db: Session):
    smsreceivers = db.query(models.SMSReceivers).all()
    return smsreceivers


def get_one(id: int, db: Session):
    smsreceiver = db.query(models.SMSReceivers).filter(models.SMSReceivers.id == id).first()
    if not smsreceiver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    return smsreceiver


def destroy(id: int, db: Session):
    smsreceiver = db.query(models.SMSReceivers).filter(models.SMSReceivers.id == id)
    if not smsreceiver.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    smsreceiver.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Receiver with id {id} has been deleted"}


def update(id: int, request: SMSReceivers, db: Session):
    smsreceiver = db.query(models.SMSReceivers).filter(models.SMSReceivers.id == id)
    if not smsreceiver.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    smsreceiver.update({"network": request.network, "criteria": request.criteria, "notification":request.notification,
                        "tel_number":request.tel_number, "name":request.name}, synchronize_session=False)
    db.commit()
    return {"detail": f"Receiver with id {id} has been updated"}