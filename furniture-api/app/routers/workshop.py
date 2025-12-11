from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/workshop", tags=["Workshop"])

@router.get("/", response_model=list[schemas.WorkshopOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Workshop).all()

@router.post("/", response_model=schemas.WorkshopOut)
def create(data: schemas.WorkshopCreate, db: Session = Depends(get_db)):
    item = models.Workshop(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
