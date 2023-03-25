from sqlalchemy.orm import Session
from .. import models
from ..schemas import Receiver
from fastapi import HTTPException, status


def create(request: Receiver, db: Session):
    new_receiver = models.Receiver(sms_category=request.sms_category, number_list=request.number_list, user_id=1)
    db.add(new_receiver)
    db.commit()
    db.refresh(new_receiver)
    return new_receiver


def get_all(db: Session):
    receivers = db.query(models.Receiver).all()
    return receivers


def get_one(id: int, db: Session):
    receiver = db.query(models.Receiver).filter(models.Receiver.id == id).first()
    if not receiver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    return receiver


def destroy(id: int, db: Session):
    receiver = db.query(models.Receiver).filter(models.Receiver.id == id)
    if not receiver.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    receiver.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Receiver with id {id} has been deleted"}


def update(id: int, request: Receiver, db: Session):
    receiver = db.query(models.Receiver).filter(models.Receiver.id == id)
    if not receiver.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Receiver with the id {id} is not found")
    receiver.update({"sms_category": request.sms_category, "number_list": request.number_list}, synchronize_session=False)
    db.commit()
    return {"detail": f"Receiver with id {id} has been updated"}